#!/usr/bin/env bash

mv  "viewer.log" "viewer.old.log"
date=`date`
echo "====================start at $date====================" >> viewer.log
nohup python ./viewer1.py ./conf/view.conf --host=10.181.41.176 >> viewer.log & # --host=192.168.7.103 

