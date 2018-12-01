"""
	File: server.py
"""
from flask import Flask, jsonify, request

CASSANDRA_SERVER_IP = "localhost"
app = Flask(__name__)


@app.route('/api/facture', methods=['POST'])
def accept_facture():
	payload = request.json
	print(payload)
	return "gab le smartass"


@app.route('/api/freqProducts', methods=['GET'])
def freq_products():
	return "Apple"


if __name__ == '__main__':
	app.run()
