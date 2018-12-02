"""
	File: server.py
"""
from flask import Flask, jsonify, request, Response
from pyspark import SparkContext, SparkConf
from pyspark.sql import SQLContext
import pymongo, json
from bson.json_util import dumps
from bson import json_util

conf = SparkConf()
conf.setAppName('appMagasin')
conf.setMaster('spark://dawg-VirtualBox:7077')
#conf.set('spark.executor.memory', '2g')
#conf.set('spark.executor.cores', '2')
#conf.set('spark.executor.instances', '2')

#conf.set("spark.jars.packages","anguenot:pyspark-cassandra:0.9.0")
#sc = SparkContext(conf=conf)
#sqlContext = SQLContext(sc)

##############################################
#	CE QUE VOUS POUVEZ MODIFIER
###
myclient = pymongo.MongoClient("mongodb://tp4:tp4tp4@ds044587.mlab.com:44587/architecture-tp4")
mydb = myclient["architecture-tp4"]

##############################################
#	A NE PAS MODIFIER
###
app = Flask(__name__)
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

