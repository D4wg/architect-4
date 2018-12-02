"""
	File: server.py
"""
from flask import Flask, jsonify, request, Response
from pyspark import SparkContext, SparkConf
from pyspark.sql import SQLContext, SparkSession
import pymongo, json
from bson.json_util import dumps
from bson import json_util

##############################################
#	CE QUE VOUS POUVEZ MODIFIER
###
MONGODB_IP="mongodb://tp4:tp4tp4@ds044587.mlab.com:44587/architecture-tp4"
MONGO_CLIENT="architecture-tp4"
SPARK_MASTER="spark://dawg-VirtualBox:7077"

##############################################
#	A NE PAS MODIFIER
###
conf = SparkConf()
conf.setAppName('appMagasin')
conf.setMaster(SPARK_MASTER)
conf.set("spark.mongodb.input.uri", MONGODB_IP)
conf.set("spark.mongodb.output.uri", MONGODB_IP)
conf.set("spark.jars.packages","org.mongodb.spark:mongo-spark-connector_2.11:2.2.5")
sc = SparkContext(conf=conf)
sqlContext = SQLContext(sc)

app = Flask(__name__)
myclient = pymongo.MongoClient(MONGODB_IP)
mydb = myclient[MONGO_CLIENT]
mycol = mydb["magasin"]

class MongoJsonEncoder(json.JSONEncoder):
	"""Hack pour stringify le json"""
	def default(self, obj):
		if isinstance(obj, (datetime.datetime, datetime.date)):
			return obj.isoformat()
		elif isinstance(obj, ObjectId):
			return unicode(obj)
		return json.JSONEncoder.default(self, obj)


@app.route('/api/facture', methods=['POST'])
def accept_facture():
	data = []
	for e in request.json:
		data.append({"productID": e['productID'], "price": e['price'], "qty": e['qty']})

	mycol.insert_one({"facture" : data })
	return ""


@app.route('/api/freqProducts', methods=['GET'])
def freq_products():
	data = dumps(mycol.find({}, {'_id': False}), default=json_util.default, cls=MongoJsonEncoder)
	return Response(data, mimetype='application/json')

if __name__ == '__main__':
	x = mycol.delete_many({})
	app.run()

