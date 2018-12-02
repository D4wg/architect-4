#!/bin/bash

HOST="$(hostname)"
SPARK_DIR=/opt/spark

$SPARK_DIR/sbin/stop-slave.sh
$SPARK_DIR/sbin/stop-master.sh

$SPARK_DIR/sbin/start-master.sh
$SPARK_DIR/sbin/start-slave.sh spark://$HOST:7077
