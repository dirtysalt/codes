#!/bin/bash

export STARROCKS_HOME=${STARROCKS_HOME}/output/be

export LIBHDFS3_CONF=${STARROCKS_HOME}/conf/core-site.xml

./libhdfs3_perf.exe --endpoint hdfs://172.26.194.238:9000 --path /user/zya/tpch_100g/orc/zlib/lineitem/ --block 128 --thread 48 --scan 200 --round 400