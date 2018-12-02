"""
	File: client.py
"""
import requests

##############################################
#	CE QUE VOUS POUVEZ MODIFIER
###
API_SERVER_URL = "http://127.0.0.1:5000/api"

##############################################
#	A NE PAS MODIFIER
###

def main():
	usrInput = ""

	while usrInput != "s":
		print("================================")
		print("Choisir une option")
		print("s: sortir")
		print("a: Ajouter une facture")
		print("r: Recuperer les items frequents")
		print("================================")
		usrInput = input("Choice: ")

		if (usrInput == "a"):
			endFactureInput = "o"
			ret = []

			while endFactureInput == "o":
				obj = {}
				obj["productID"] = int(input("Id du produit (int): "))
				obj["price"] = float(input("Prix (float): "))
				obj["qty"] = int(input("Quantite (int): "))
				ret.append(obj)

				print("continuer? (o/n)")
				endFactureInput = input()

			print("CALLING " + API_SERVER_URL + "/facture")
			r = requests.post(API_SERVER_URL + "/facture", json=ret)
			print(r.text)

		elif (usrInput == "r"):
			print("CALLING " + API_SERVER_URL + "/freqProducts")
			r = requests.get(API_SERVER_URL + "/freqProducts")
			print(r.text)

if __name__ == '__main__':
	main()
