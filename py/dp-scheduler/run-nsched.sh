#!/usr/bin/env bash
#Copyright (C) dirlt

rm -f nsched.log 
date=`date`
echo "====================start at $date====================" >> nsched.log
nohup ./nsched.py ./conf/nsched.sample.conf --host=127.0.0.1 $* >> nsched.log &


