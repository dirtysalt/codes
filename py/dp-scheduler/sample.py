#!/usr/bin/env python
#coding:utf-8
#Copyright (C) dirlt

import sys
import os
sys.path.append('./lib')
import time
import json

from api import *

client=Client('127.0.0.1',8000)

jid = int(time.time())

job=Job()
jobName='TestMR#%d'%(jid)
job.setJobName(jobName)
job.setCommand('cat nothing')
job.setDep(["and",{"file-ready":"/home/dirlt/_SUCCESS"}])
print client.submitJob(job)

jid+=1
jobName='TestMR#%d'%(jid)
job.setJobName(jobName)
job.setCommand('sleep 5')
job.setDep(["and",{"file-ready":"/home/dirlt/_SUCCESS"}, {"job-status@TestMR#%d"%(jid-1):"success"}])
client.submitJob(job)

jid+=1
jobName='echo#%d'%(jid)
job.setJobName(jobName)
job.setCommand('echo "hello"')
job.setDep({"lagtime":1, "rest":["and",{"file-ready":"/home/dirlt/_SUCCESS2"}, {"job-status@TestMR#%d"%(jid-1):"success"}]})
job.setSchedTime(convertDateTimeToTimeStamp('2012-12-31 00:00:00'))
client.submitJob(job)
