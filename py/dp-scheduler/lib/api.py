#!/usr/bin/env python
#coding:utf-8
#Copyright (C) dirlt

import urllib2
import urllib
from job import Job, convertDateTimeToTimeStamp, convertTimeStampToDateTime
from util import raiseHTTPRequest

class Client(object):
    def __init__(self,host,port,http_to=5):
        self._host=host
        self._port=port
        self._url='http://%s:%d/'%(host,port)
        self._http_to=http_to

    def getPostData(self,job):
        return str(job)

    def urlescape(self,s):
        return urllib.quote(s)
    
    def submitJob(self,job):
        assert(isinstance(job,Job))
        return raiseHTTPRequest(self._url+'submit',
                                 self.getPostData(job)
                                 ,self._http_to)

    def deleteJob(self,jobName):
        return raiseHTTPRequest(self._url+'delete?id=%s'%(self.urlescape(jobName)),
                                 timeout=self._http_to)

    
    def forceStartJob(self,jobName):
        return raiseHTTPRequest(self._url+'fstart?id=%s'%(self.urlescape(jobName)),
                                 timeout=self._http_to)

    def queryJobsDependOn(self,jobName):
        return raiseHTTPRequest(self._url+'dep?id=%s'%(self.urlescape(jobName)),
                                 timeout=self._http_to)

    def alterJob(self,job):
        assert(isinstance(job,Job))
        return raiseHTTPRequest(self._url+'alter',
                                 self.getPostData(job)
                                 ,self._http_to)

    def view(self):
        return raiseHTTPRequest(self._url+'view',
                                 timeout=self._http_to)


