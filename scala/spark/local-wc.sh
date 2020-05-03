#!/usr/bin/env bash
#Copyright (C) dirlt

MASTER="spark://localhost:7077"
#MASTER="local[4]"
OPTS="--conf spark.eventLog.enabled=true"
spark-submit --master $MASTER $OPTS --class LocalWordCount target/spark-test-1.0-SNAPSHOT-jar-with-dependencies.jar
