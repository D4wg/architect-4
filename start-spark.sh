#!/bin/bash
exec 3> /dev/null

#######
# Peut modifier
####
SPARK_DIR=/opt/spark

#######
# A ne pas modifier
####
HOST="$(hostname)"

echo -e "##############################"
echo -e "Current host: " $HOST
echo -e "Spark dir:    " $SPARK_DIR
echo -e "##############################\n"

echo -e "\nSetting the spark-env.sh"
cp $SPARK_DIR/conf/spark-env.sh.template $SPARK_DIR/conf/spark-env.sh
echo -e "SPARK_WORKER_INSTANCES=2\nSPARK_WORKER_CORES=1" > $SPARK_DIR/conf/spark-env.sh

echo -e "\nStopping current spark master and slaves"
$SPARK_DIR/sbin/stop-slave.sh
$SPARK_DIR/sbin/stop-master.sh

echo -e "\nRunning spark master and slaves"
$SPARK_DIR/sbin/start-master.sh
$SPARK_DIR/sbin/start-slave.sh spark://$HOST:7077

echo -e "\nDone"
