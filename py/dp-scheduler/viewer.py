#!/usr/bin/env python
#coding:utf-8
#Copyright (C) dirlt

import sys
import os
dir=os.path.dirname(__file__)
sys.path.append(os.path.join(dir,'lib'))

# to reuse address.
import SocketServer
SocketServer.BaseServer.allow_reuse_address=True
SocketServer.TCPServer.allow_reuse_address=True

def usage(prog):
    print 'viewer'
    print 'usage:%s <path-to-nsched.conf>'%(prog)

from mysqldb import JobDataBase,JobDataBasePool
from http import HTTPServer
from util import SimpleConfig,getLogger


def main(argv):
    host = ''
    port = 0
    dbhost=''
    dbname=''
    argv_ = []
    for arg in argv:
        if(arg.startswith('--host=')):
            host = arg[len('--host='):]
        elif(arg.startswith('--port=')):
            port = int(arg[len('--port='):])
        elif(arg.startswith('--dbhost=')):
            dbhost = arg[len('--dbhost='):]
        elif(arg.startswith('--dbname=')):
            dbname = arg[len('--dbname='):]
        else:
            argv_.append(arg)
    argv = argv_
    if(len(argv)!=2):
        usage(argv[0])
        sys.exit(-1)

    logger=getLogger('nsched')
    conf=SimpleConfig()
    if(not os.path.isfile(argv[1])):
        logger.fatal("file('%s') not exists",argv[1])
        sys.exit(-1)

    conf.readFile(argv[1])
    env=conf.copyOut()
    # override port.
    if(host):
        env['nsched.http-host']=host
    if(port):
        env['nsched.http-port']=port
    if(dbname):
        env['nsched.db-name']=dbname
    if(dbhost):
        env['nsched.db-host']=dbhost

    # mkdir log dir.
    if(not os.path.exists(env['nsched.log-dir'])):
       os.makedirs(env['nsched.log-dir'])

    # reset default value.
    # TODO(dirlt):
    env['_logger']=logger

    # create db.
    db=JobDataBase(env)
    db.createTable()
    dbPool=JobDataBasePool(db)
    env['_db']=dbPool

    # http server.
    http=HTTPServer(env,admin=True)
    http.run()

if __name__=='__main__':
    main(sys.argv)


