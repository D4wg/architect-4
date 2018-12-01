"""
	File: client.py
"""
import requests

API_SERVER_URL = "http://127.0.0.1:5000/api"
facture = [
	{"name": "grape", "price": 4.99, "qty": 2},
	{"name": "apple", "price": 2.99, "qty": 3},
	{"name": "orange", "price": 3.99, "qty": 4}
]


def main():
	print("CALLING " + API_SERVER_URL + "/freqProducts")
	r = requests.get(API_SERVER_URL + "/freqProducts")
	print(r.text)

	print("CALLING " + API_SERVER_URL + "/facture")
	r = requests.post(API_SERVER_URL + "/facture", json=facture)
	print(r.text)

	print("CALLING " + API_SERVER_URL + "/freqProducts")
	r = requests.get(API_SERVER_URL + "/freqProducts")
	print(r.text)

if __name__ == '__main__':
	main()
