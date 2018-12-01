"""
	File: server.py
"""
from flask import Flask, jsonify, request
from cassandra.cluster import Cluster

##############################################
#	CE QUE VOUS POUVEZ MODIFIER
###
CASSANDRA_SERVER_IP = "localhost"

##############################################
#	A NE PAS MODIFIER
###
app = Flask(__name__)
cluster = Cluster([CASSANDRA_SERVER_IP], port=9042)
session = cluster.connect()

@app.route('/api/facture', methods=['POST'])
def accept_facture():
	payload = request.json
	#print(payload)
	return "gab le smartass"


@app.route('/api/freqProducts', methods=['GET'])
def freq_products():
	query = "SELECT * FROM facture"

	future = session.execute_async(query)
	rows = future.result()

	ret = []

	for res in rows:
		ret.append({"factureID": res.factureid, "productID": res.productid, "price": res.price, "qty": res.qty})
		print("{0}\t{1}\t{2}".format(res.id, res.factureid, res.price))

	return jsonify(ret)


if __name__ == '__main__':
	session.execute("CREATE KEYSPACE IF NOT EXISTS magasin WITH REPLICATION = { 'class' : 'SimpleStrategy', 'replication_factor' : 3 };")
	session.set_keyspace('magasin')
	
	session.execute("""CREATE TABLE IF NOT EXISTS facture(
		id uuid PRIMARY KEY,
		factureID int,
		productID int,
		price float,
		qty int);""")

	#session.execute("""INSERT INTO facture (id, factureID, productID, price, qty) VALUES (uuid(), 0, 1, 4.99, 1);""")
	app.run()
