#!/usr/bin/env python
#coding:utf-8

import requests
import time
import sys
import json
now = time.strftime("%Y-%m-%d %H:%M:%S")
args = sys.argv[1:]
HOST = args[0]
PORT= args[1]
jobName = args[2]
info = {
    "type":"JOBLAG",
    "desc":"run job delay",
    "host": HOST,
    "itemkey": now,
    "msg": jobName
    }
headers = {'content-type' : 'application/json'}
r = requests.post("http://dp0:50000/sendsms/json/",data=json.dumps(info), headers=headers)
#print r
