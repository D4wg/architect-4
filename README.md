# TP4 ARCHITECTURE
> Intégration de spark dans un service rest écrit en python 2.7.

## Pre requis
1. Sur ubuntu 18.04, avoir git et python2 avec pip avec les commandes suivantes:
    - `sudo apt update`
    - `sudo apt install git python-pip`
2. Clonez ce repo git:
    - `git clone https://github.com/D4wg/architect-4.git`
3. Roulez les commandes suivantes (Peut prendre 5 min):
    - `cd architect-4/`
    - `pip install -r requirements.txt`
4. Installer Cassendra et le rouler si ce n'est pas fait en localhost.
5. [Installer Spark 2.4.0](https://medium.com/@josemarcialportilla/installing-scala-and-spark-on-ubuntu-5665ee4b62b1)
6. Dans le dossier spark (/opt/spark/).
    - ajouter dans un fichier spark-env.sh situé dans le dossier conf/:
        >SPARK_WORKER_INSTANCES=2

        >SPARK_WORKER_CORES=1
    
    - Rouler le master avec cette commande: `sudo ./sbin/start-master.sh`
    - Aller à l'adresse localhost:8080 et retenez le lien affiché sous la forme `spark://<hostname>:7077` pour la prochaine commande.
    - Rouler les slaves avec cette commande: `sudo ./sbin/start-slave.sh spark://<hostname>:7077`

## Rouler le service et le client
Dans le dossier de ce repo git, faire partir le serveur python:
- `python server.py`

Partir le client python dans un autre terminal:
- `python client.py`
