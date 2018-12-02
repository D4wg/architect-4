"""
	File: server.py
"""
from flask import Flask, jsonify, request
from cassandra.cluster import Cluster
from pyspark import SparkContext, SparkConf
from pyspark.sql import SQLContext, Row
from pyspark.mllib.fpm import FPGrowth
import os

conf = SparkConf().setAppName('AppMagasin').setMaster('spark://' + os.uname()[1] + ':7077')
conf.set("spark.jars.packages","anguenot:pyspark-cassandra:0.9.0")
sc = SparkContext(conf=conf)
sqlContext = SQLContext(sc)


##############################################
#	CE QUE VOUS POUVEZ MODIFIER
###
CASSANDRA_SERVER_IP = "localhost"

##############################################
#	A NE PAS MODIFIER
###
app = Flask(__name__)
cluster = Cluster()
session = cluster.connect()


@app.route('/api/facture', methods=['POST'])
def accept_facture():
	future = session.execute_async("SELECT MAX(factureID) AS currows FROM facture;")
	rows = future.result().one()

	curRow = rows.currows + 1 if rows[0] != None else 0

	payload = request.json
	for facture in payload:
		print(facture)
		facture["factureID"] = curRow	# Add an additionnal attribute
		session.execute("""INSERT INTO facture (id, factureID, productID, price, qty) 
			VALUES (uuid(), %(factureID)s, %(productID)s, %(price)s, %(qty)s);""", facture)

	return ""


@app.route('/api/freqProducts', methods=['GET'])
def freq_products():
	try:
		factures = sqlContext.read \
			.format("org.apache.spark.sql.cassandra") \
			.options(table="facture", keyspace="magasin") \
			.load()
		
		factures.show()

		model = FPGrowth.train(factures.rdd.map(lambda x: list(set(x))), minSupport=0.2, numPartitions=10)
		result = model.freqItemsets().collect()
		for fi in result:
			print(fi)
	except Exception as e:
		print(e)

	return jsonify(result)


if __name__ == '__main__':
	session.execute("CREATE KEYSPACE IF NOT EXISTS magasin WITH REPLICATION = { 'class' : 'SimpleStrategy', 'replication_factor' : 3 };")
	session.set_keyspace('magasin')
	
	#session.execute("""DROP TABLE facture""")

	session.execute("""CREATE TABLE IF NOT EXISTS facture(
		id uuid PRIMARY KEY,
		factureID int,
		productID int,
		price float,
		qty int);""")

	#session.execute("""INSERT INTO facture (id, factureID, productID, price, qty) VALUES (uuid(), 0, 1, 4.99, 1);""")
	
	app.run()
