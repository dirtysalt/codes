#!/usr/bin/env python
#coding:utf-8
#Copyright (C) dirlt

import time
import json

def convertDateTimeToTimeStamp(s):
    st = time.strptime(s,'%Y-%m-%d %H:%M:%S')
    return int(time.mktime(st))

def convertTimeStampToDateTime(ts):
    # in seconds.
    st = time.localtime(int(ts))
    return time.strftime('%Y-%m-%d %H:%M:%S',st)

class Job(object):
    kMapReduceJobPrefix='MR.'
    @staticmethod
    def isMRJob(jobName):
        if(jobName.startswith(Job.kMapReduceJobPrefix)):
            return True
        k=jobName.split('#')[0]
        if(k.endswith('MR')):
            return True
        return False
    
    def __init__(self):
        self._dep=[]
        self._schedTime=int(time.time())
        self._blockDesc=''
        
    def setBlockDesc(self,blockDesc):
        self._blockDesc=blockDesc
    def blockDesc(self):
        return self._blockDesc
    
    def setJobName(self,jobName):
        self._jobName=jobName
    def jobName(self):
        return self._jobName

    def setCommand(self,command):
        self._command=command
    def command(self):
        return self._command

    # json object.
    def setDep(self,dep):
        self._dep=dep
    def dep(self):
        return self._dep

    def setSchedTime(self,schedTime):
        self._schedTime=int(schedTime)
    def schedTime(self):
        return self._schedTime
    
    def notChanged(self,x):
        return self._jobName == x.jobName() and \
               self._command == x.command() and \
               self._dep == x.dep() and \
               self._schedTime == x.schedTime()

    # a pair function with readin.
    def __repr__(self):
        content = {}
        fields=('jobName','command','dep','schedTime')
        for f in fields:
            method = f
            content[f]=self.__getattribute__(method)()
        return json.dumps(content)

    @staticmethod
    def readin(js):
        job=Job()
        fields=('jobName','command','dep','schedTime')
        for f in fields:
            if(f in js):
                method='set'+f[0].upper()+f[1:]
                job.__getattribute__(method)(js[f])
        return job

    @staticmethod
    def readFromDB(row):
        job=Job()
        fields=('jobName','command','dep','schedTime')
        for i in range(len(fields)):
            f=fields[i]
            c=row[i]
            method='set'+f[0].upper()+f[1:]
            v = str(c)
            if(f == 'dep'):
                v = json.loads(v)
            job.__getattribute__(method)(v)
        return job

    @staticmethod
    def unittest():    
        job=Job()
        job.setJobName("HourlyProcedure#2012080920")
        job.setCommand("java com.umeng.dp.comproc.comproc-with-dependencies.jar com.umeng.dp.comproc.HourlyProcedure 2012080920")
        job.setDep(["and",{"lagtime":120}]) # in json expression.
        job.setSchedTime(convertDateTimeToTimeStamp('2012-08-08 20:00:00'))
        js=str(job)
        job2=Job.readin(json.loads(js))
        assert(job.notChanged(job2))
               
if __name__=='__main__':
    Job.unittest()
    
        
    
