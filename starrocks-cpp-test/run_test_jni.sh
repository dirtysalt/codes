#!/bin/bash

export STARROCKS_HOME=$HOME/StarRocks/output/be
export HADOOP_CLASSPATH=${STARROCKS_HOME}/lib/hadoop-lib/hadoop-lib/*:${STARROCKS_HOME}/lib/hadoop/common/*:${STARROCKS_HOME}/lib/hadoop/common/lib/*:${STARROCKS_HOME}/lib/hadoop/hdfs/*:${STARROCKS_HOME}/lib/hadoop/hdfs/lib/*
export CLASSPATH=${STARROCKS_HOME}/lib/jni-packages/starrocks-hadoop-ext.jar:$STARROCKS_HOME/conf:$STARROCKS_HOME/lib/jni-packages/*:$HADOOP_CLASSPATH:$CLASSPATH
export LD_LIBRARY_PATH=$STARROCKS_HOME/lib/hadoop-lib/native:$STARROCKS_HOME/lib/hadoop/native:$LD_LIBRARY_PATH
./test_jni.exe