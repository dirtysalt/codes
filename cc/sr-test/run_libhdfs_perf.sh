#!/bin/bash

export LD_LIBRARY_PATH=$JAVA_HOME/lib/server:$JAVA_HOME/lib:$LD_LIBRARY_PATH

export STARROCKS_HOME=${STARROCKS_HOME}/output/be

export HADOOP_CLASSPATH=${STARROCKS_HOME}/lib/hadoop/common/*:${STARROCKS_HOME}/lib/hadoop/common/lib/*:${STARROCKS_HOME}/lib/hadoop/hdfs/*:${STARROCKS_HOME}/lib/hadoop/hdfs/lib/*

export CLASSPATH=$STARROCKS_HOME/conf:$HADOOP_CLASSPATH:$CLASSPATH

export LIBHDFS3_CONF=${STARROCKS_HOME}/conf/core-site.xml

./libhdfs_perf.exe --endpoint hdfs://172.26.194.238:9000 --path /user/zya/tpch_100g/orc/zlib/lineitem/ --block 128 --thread 48 --scan 200 --round 400