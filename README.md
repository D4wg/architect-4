Prereq: `jdk8-openjdk jre8-openjdk`

Installer python sur Ubuntu:
- `sudo apt install update`
- `sudo apt install python3`
- `sudo apt install python3-pip`

Installer les dependances python necessaires (Peut prendre 5 min):
- `pip3 install -r requirements.txt`

>Note: si vous avez python 2 et 3, il faut remplacer la commande pip par pip3.

Assurer que le service de cassandra roule. Par defaut, le serveur va prendre localhost.

Commencer le serveur python:
- `python3 server.py`

Commencer le client python:

- `python3 client.py`

