#!/usr/bin/env python
#coding:utf-8
#Copyright (C) dirlt

import threading
import multiprocessing
import Queue
import time
import os
import subprocess
import re
import urllib

from job import Job
from util import exceptionToString,getLogger,rotateFile,nsched_notify
#from db import JobDataBasePool
from mysqldb import JobDataBasePool

class Task(object):
    def __init__(self,env,callback,model=threading.Thread):
        self._logger=env['_logger']
        self._number=int(env['nsched.task-thread-number'])
        self._queue_size=int(env['nsched.task-queue-size'])
        self._timeout = int(env['nsched.task-queue-timeout'])
        self._model=model
        self._queue=Queue.Queue(self._queue_size)
        self._exit=False
        def proxy_callback():
            while(True):
                if(self._exit):
                    break
                try:
                    request=self._queue.get(True,self._timeout * 1.0 / 1000)
                except Queue.Empty,_: # no item.
                    continue
                callback(request)

        self._callback=proxy_callback
        self._collection=[]

    def putRequest(self,request):
        self._queue.put(request)

    def start(self):
        self._exit=False
        for i in range(0,self._number):
            # start thread.
            run=self._model(target=self._callback,
                            name='Task%d'%(i))
            self._collection.append(run)
            run.start()

    def stop(self):
        self._logger.info('stop task...')
        self._exit=True
        for run in self._collection:
            run.join()


def makeJobRequest(jobName,cmd,env):
    return RunLocalJobRequest(jobName,cmd,env)

class RunLocalJobRequest(object):
    def __init__(self,jobName,cmd,env):
        self._jobName=jobName
        self._cmd=cmd
        self._env=env

    def run(self):
        errlog = os.path.join(self._env['nsched.log-dir'],self._jobName+'.stderr')
        outlog = os.path.join(self._env['nsched.log-dir'],self._jobName+'.stdout')
        rotateFile(errlog)
        rotateFile(outlog)
        errf = open(errlog,'wb')
        outf = open(outlog,'wb')
        p=subprocess.Popen(self._cmd,shell=True,bufsize=0,
                           stdin=subprocess.PIPE,
                           stdout=outf,
                           stderr=errf,
                           close_fds=True)
        p.wait()
        self._code=p.returncode
        errf.close()
        outf.close()
        return self._code

    def reportFailure(self,s):
        host=os.uname()[1]
        subject="[nsched@%s]RUN JOB FAILED '%s'"%(host, self._jobName)
        jobName=urllib.quote(self._jobName)
        # text = "checkout details: http://%s:%s/view?pattern=%s&refresh=-1"%(
        #     self._env['nsched.http-host'],
        #     self._env['nsched.http-port'],
        #     jobName)
        text = 'RT'
        if not os.path.exists(self._env['nsched.notify.no-report-file']):
            nsched_notify(self._env,subject,text)

    def getJobStatus(self):
        if(self._code == 0):
            return 'SUCCESS'
        return 'FAILED'

    def jobName(self):
        return self._jobName

    def globalEnv(self):
        return self._env

    def command(self):
        return self._cmd

def _callback(request):
    # must be subclass of job request.
    assert(isinstance(request,RunLocalJobRequest))
    jobName=request.jobName()
    env=request.globalEnv()
    retry=int(env['nsched.submit-retry'])
    logger=env['_logger']
    db=env['_db'].instance()

    logger.info("start job(%s)",jobName)
    code=request.run()  # wait for completion.
    logger.debug('request complete code(%d)'%(code))
    es = None
    status = 'SUCCESS'

    while(True):
        try:
            status=request.getJobStatus()
            logger.debug('request.getJobStatus(%s)=%s'%(jobName,status))
            if (status =='FAILED'): # submit failed.
                retry-=1
                # don't retry it.
                if (os.path.exists(env['nsched.no-retry-file'])):
                    retry = -1

                if(retry<0):
                    status = 'FAILED'
                    break
                else:
                    # resubmit.
                    logger.info("retry(%d) job(%s)", retry, jobName)
                    code=request.run() # wait for completion.
                    logger.debug("request complete code(%d)"%(code))
                    continue

            elif(status=='SUCCESS'): # nothing happens.
                break

        except Exception,_:
            logger.debug('caught exception %s', es)
            break

    if(status!='SUCCESS'):
        request.reportFailure(es)
        db.incJobFailedTime(jobName)

    assert(status in ('FAILED','SUCCESS'))
    db.updateJobStatus(jobName, status)
    db.updateJobEndTime(jobName,time.time())

class RunJobTask(Task):
    def __init__(self,env):
        Task.__init__(self,env,_callback)

def _callback2(request):
    try:
        request()
    except Exception,_:
        pass

class RunCallableTask(Task):
    def __init__(self,env):
        Task.__init__(self,env,_callback2)


