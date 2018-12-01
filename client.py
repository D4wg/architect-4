"""
	File: client.py
"""
import requests

##############################################
#	CE QUE VOUS POUVEZ MODIFIER
###
API_SERVER_URL = "http://127.0.0.1:5000/api"
facture = [
	{"productID": 1, "price": 4.99, "qty": 2},
	{"productID": 2, "price": 2.99, "qty": 3},
	{"productID": 3, "price": 3.99, "qty": 4}
]

##############################################
#	A NE PAS MODIFIER
###

def main():
	print("CALLING " + API_SERVER_URL + "/freqProducts")
	r = requests.get(API_SERVER_URL + "/freqProducts")
	print(r.text)
	
	"""
	print("CALLING " + API_SERVER_URL + "/facture")
	r = requests.post(API_SERVER_URL + "/facture", json=facture)
	print(r.text)

	print("CALLING " + API_SERVER_URL + "/freqProducts")
	r = requests.get(API_SERVER_URL + "/freqProducts")
	print(r.text)
	"""

if __name__ == '__main__':
	main()
