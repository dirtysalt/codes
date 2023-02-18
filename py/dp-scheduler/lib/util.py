#!/usr/bin/env python
#coding:utf-8
#Copyright (C) dirlt

import string
import copy
import smtplib,email
from email.MIMEText import MIMEText
import threading
import logging
import sys
import traceback
import urllib2
import os
import socket
import fcntl
import struct
import json
import httplib

# simple config
class SimpleConfig:
    def __init__(self):
        self._dict={}

    def readFile(self,filename):
        content=open(filename).read()
        self.readString(content)

    def readString(self,content):
        xs=filter(lambda x:x and x[0]!='#',
                  map(lambda x:string.strip(x),
                      content.split('\n')))
        for x in xs:
            (k,v)=map(lambda x:string.strip(x),x.split('=',1))
            self._dict[k]=v

    def __getitem__(self,k):
        return self._dict[k]

    def __setitem__(self,k,v):
        self._dict[k]=v

    def has_key(self,k):
        return (k in self._dict)

    def keys(self):
        return self._dict.keys()

    def size(self):
        return len(self._dict)

    def writeString(self):
        return '\n'.join(map(lambda x:x[0] + ' = ' + x[1],self._dict.items()))

    def writeFile(self,filename):
        content=self.writeString()+'\n'
        open(filename,'w').write(content)

    def copyOut(self):
        return copy.deepcopy(self._dict)

    @staticmethod
    def unittest():
        sf=SimpleConfig()
        sf.readString("# comment\nkey1 = value1\nkey2 = value2\n")
        assert(sf['key1']=='value1')
        assert(sf['key2']=='value2')
        content=sf.writeString()

        sf.readString(content)
        assert(sf['key1']=='value1')
        assert(sf['key2']=='value2')

class NopLock(object):
    def __init__(self):
        pass
    def lock(self):
        pass
    def unlock(self):
        pass

class MutexThreadLock(object):
    def __init__(self):
        self._lock=threading.Lock()

    def lock(self):
        self._lock.acquire()

    def unlock(self):
        self._lock.release()

def raiseHTTPRequest(url,data=None,timeout=3):
    # if we do post, we have to provide data.
    f=urllib2.urlopen(url,data,timeout)
    return f.read()

def nsched_notify(env,subject,text,group='RT'):
    if not ('nsched.notify.enable' in env and env['nsched.notify.enable']):
        return
    # subject as id to be deduplicated.
    js = { #'id':subject,
          'tool':'mail',
          'group':group,
          'type':'normal',
          'title':subject,
          'content':text}
    host=env['nsched.notify.host']
    port=env['nsched.notify.port']
    print host,port
    # TODO(dirlt):POST HTTP.
    data=json.dumps(js)
    print data

    conn = httplib.HTTPConnection(host,int(port),timeout=3)
    try:
        conn.connect()
        conn.sock.settimeout(3) # 3 seconds.
        conn.request('POST','/let/fire',data,
                     {'Content-Type':'application/json'})
        data2=conn.getresponse().read()
        print 'nsched_notify OK'
        print data2
    except Exception,e:
        print 'nsche_notify FAILED'
        print e
    finally:
        conn.close()

def getLogger(name):
    FORMAT = '%(asctime)-15s %(threadName)s [%(levelname)s] [%(name)s] %(funcName)s@%(filename)s:%(lineno)d %(message)s'
    #logging.basicConfig(format=FORMAT,filename=logfile)
    logging.basicConfig(format=FORMAT)
    logger=logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    return logger

def exceptionToString():
    exc_type, exc_value, exc_traceback = sys.exc_info()
    err=''.join(traceback.format_exception(exc_type, exc_value, exc_traceback))
    return err

def rotateFile(f):
    idx = 0
    if (not os.path.exists(f)):
        return
    while True:
        nf = '%s.%d'%(f,idx)
        if (not os.path.exists(nf)):
            os.rename(f,nf)
            return
        idx += 1

def getIpAddress(ifname):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    return socket.inet_ntoa(fcntl.ioctl(
        s.fileno(),
        0x8915,  # SIOCGIFADDR
        struct.pack('256s', ifname[:15])
    )[20:24])

if __name__=='__main__':
    SimpleConfig.unittest()

    env = {'nsched.notify.enable':'1',
           'nsched.notify.host':'dp0',
           'nsched.notify.port':'57004'}
    nsched_notify(env, '调度器测试','内容', 'RT')

