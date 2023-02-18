#!/usr/bin/env python
#coding:utf-8
#Copyright (C) dirlt

####Reminder: db.py not used anymore

# sudo apt-get install sqlite
import sqlite3
import json
import threading

from job import Job,convertDateTimeToTimeStamp,convertTimeStampToDateTime
from util import MutexThreadLock,getLogger
kMaxSchedTime = convertDateTimeToTimeStamp('3000-01-01 00:00:00')

# really nasty nasty code.
# a sqlite object can't be used in multi thread.
# I have to admit, it don't know how to use SQL.
# and it doesn't deny that sqlite api sucks.
class JobDataBasePool(object):
    def __init__(self,db):
        self._db=db
        self._dict={}
    def instance(self):
        tid=threading.currentThread().ident
        if(tid in self._dict):
            return self._dict[tid]
        clone=self._db.clone()
        self._dict[tid]=clone
        return clone

class JobDataBase(object):
    def __init__(self,env,lock=MutexThreadLock):
        self._env=env
        self._logger=env['_logger']
        self._dbfile=env['nsched.db']
        self._lock=lock()
        self._conn=sqlite3.connect(self._dbfile)
        self._cursor=self._conn.cursor()

    def close(self):
        self._conn.close()

    def clone(self):
        # so we clone a object, but share a lock.
        db=JobDataBase(self._env)
        db._lock=self._lock # share a lock.
        return db

    def dropTable(self):
        try:
            self._lock.lock()
            SQL="DROP TABLE IF EXISTS jobTable";
            self._cursor.execute(SQL)
            self._conn.commit()
        finally:
            self._lock.unlock()

    def createTable(self):
        schema="""(
        jobName text PRIMARY KEY,
        command text,
        dep text,
        schedTime int,
        status text,
        force text,
        startTime int,
        endTime int,
        description text,
        jobId text,
        failedTime int
        )"""
        SQL="CREATE TABLE IF NOT EXISTS jobTable %s"%(schema)
        try:
            self._lock.lock()
            self._cursor.execute(SQL)
            self._conn.commit()
        finally:
            self._lock.unlock()

    def isJobExisted(self,jobName):
        SQL="SELECT * FROM jobTable WHERE jobName=?"
        self._cursor.execute(SQL,(jobName,))
        return self._cursor.fetchone()

    def _queryJobStatus(self,jobName):
        # SUCCESS
        # KILLED
        # WAITING
        # RUNNING
        # NONE->FAILED.
        # NONE WILL NOT STORED IN DB.
        SQL="SELECT status FROM jobTable WHERE jobName=?"
        self._cursor.execute(SQL,(jobName,))
        for r in self._cursor:
            return r[0]
        return 'NONE'

    def queryJobStatus(self,jobName):
        try:
            self._lock.lock()
            return self._queryJobStatus(jobName)
        finally:
            self._lock.unlock()

    def addJob(self,job):
        try:
            # check whether the job exists.
            self._lock.lock()
            if(self.isJobExisted(job.jobName())):
                return 'job(%s) is existed'%(job.jobName())
            # workaround.
            # if schedTime is too much
            # I think our intention is to let job start manually.
            status = 'WAITING'
            if(job.schedTime() >= kMaxSchedTime):
                job.setSchedTime(0)
                status = 'KILLED'
            SQL="INSERT INTO jobTable values(?,?,?,?,?,'false',0,0,'','',0)"
            self._cursor.execute(SQL,(job.jobName(),
                                      job.command(),
                                      json.dumps(job.dep()),
                                      job.schedTime(),
                                      status))
            self._conn.commit()
            return 'OK'
        finally:
            self._lock.unlock()

    def deleteJob(self,jobName):
        try:
            # check whether the job exists.
            self._lock.lock()
            if(not self.isJobExisted(jobName)):
                return 'job(%s) is not existed'%(jobName)
            # whether running.
            status=self._queryJobStatus(jobName)
            if(status == 'RUNNING'):
                return 'job(%s) is running'%(jobName)
            SQL="DELETE FROM jobTable WHERE jobName=?"
            self._cursor.execute(SQL,(jobName,))
            self._conn.commit()
            return 'OK'
        finally:
            self._lock.unlock()

    def updateJob(self,job):
        try:
            # check whether the job exists.
            self._lock.lock()
            if(not self.isJobExisted(job.jobName())):
                return 'job(%s) is not existed'%(job.jobName())
            # whether running.
            status=self._queryJobStatus(job.jobName())
            if(status == 'RUNNING'):
                return 'job(%s) is running'%(job.jobName())
            SQL="UPDATE jobTable SET command=?, dep=?, schedTime=? WHERE jobName=?"
            self._cursor.execute(SQL,(job.command(),
                                      json.dumps(job.dep()),
                                      job.schedTime(),
                                      job.jobName()))
            self._conn.commit()
            return 'OK'
        finally:
            self._lock.unlock()

    def forceStartJob(self,jobName):
        try:
            # check whether the job exists.
            self._lock.lock()
            if(not self.isJobExisted(jobName)):
                return 'job(%s) is existed'%(jobName)
            # whether running.
            status=self._queryJobStatus(jobName)
            if(status == 'RUNNING'):
                return 'job(%s) is running'%(jobName)
            SQL="UPDATE jobTable SET force='true' WHERE jobName=?"
            self._cursor.execute(SQL,(jobName,))
            self._conn.commit()
            return 'OK'
        finally:
            self._lock.unlock()

    def isJobForcedStart(self,jobName):
        try:
            # check whether the job exists.
            self._lock.lock()
            if(not self.isJobExisted(jobName)):
                return False
            SQL="SELECT force from jobTable WHERE jobName=?"
            self._cursor.execute(SQL,(jobName,))
            row=self._cursor.fetchone()
            return row[0]=='true'
        finally:
            self._lock.unlock()

    def restartJob(self,jobName):
        try:
            # check whether the job exists.
            self._lock.lock()
            if(not self.isJobExisted(jobName)):
                return 'job(%s) is not existed'%(jobName)
            # whether running.
            status=self._queryJobStatus(jobName)
            if(status == 'RUNNING'):
                return 'job(%s) is running'%(jobName)
            self._cursor.execute("UPDATE jobTable SET status='WAITING', force='false', startTime=0, endTime=0 WHERE jobName=?",(jobName,))
            self._conn.commit()
            return 'OK'
        finally:
            self._lock.unlock()

    def successJob(self,jobName):
        try:
            # check whether the job exists.
            self._lock.lock()
            if(not self.isJobExisted(jobName)):
                return 'job(%s) is not existed'%(jobName)
            # whether running.
            status=self._queryJobStatus(jobName)
            if(status == 'RUNNING'):
                return 'job(%s) is running'%(jobName)
            self._cursor.execute("UPDATE jobTable SET status='SUCCESS', force='false', startTime=0, endTime=0 WHERE jobName=?",(jobName,))
            self._conn.commit()
            return 'OK'
        finally:
            self._lock.unlock()

    def killJob(self,jobName):
        try:
            # check whether the job exists.
            self._lock.lock()
            if(not self.isJobExisted(jobName)):
                return 'job(%s) is not existed'%(jobName)
            # whether running.
            status=self._queryJobStatus(jobName)
            if(status == 'RUNNING'):
                return 'job(%s) is running'%(jobName)
            self._cursor.execute("UPDATE jobTable SET status='KILLED', force='false', startTime=0, endTime=0 WHERE jobName=?",(jobName,))
            self._conn.commit()
            return 'OK'
        finally:
            self._lock.unlock()

    def queryAllJob(self,pattern='',page=-1,per=50):
        try:
            self._lock.lock()

            if (pattern=='UNSUCCESS'):
                return self.queryAllUnsuccessJob(page,per)

            # if pattern are followings, we search by status.
            field = 'jobName'
            if(pattern in ('RUNNING','KILLED','FAILED','SUCCESS','WAITING')):
                field = 'status'

            # ugly...
            if(not pattern):
                self._cursor.execute("SELECT COUNT(*) from jobTable")
            else:
                self._cursor.execute("SELECT COUNT(*) from jobTable WHERE %(field)s LIKE ?"%(locals()),
                                     ('%'+pattern+'%',))
            r=self._cursor.fetchone()
            count = r[0]

            # just return count.
            if (page==-1):
                return count

            # watch out, bugs come here.
            pages = (count + per - 1) / per;
            limit = per;
            if(page == (pages - 1)): # last page.
                limit = count - page * per;

            if(not pattern):
                self._cursor.execute("SELECT * from jobTable LIMIT ?  OFFSET ?",
                                     (limit, count - page*per - per))
            else:
                self._cursor.execute("SELECT * from jobTable WHERE %(field)s LIKE ? LIMIT ? OFFSET ?"%(locals()),
                                     ('%'+pattern+'%',limit,count - page*per - per))
            result=[]
            for r in self._cursor:
                result.append(r)
            # TODO(dirlt): reverse in SQL.
            result=result[::-1]

            # return result.
            return (result,count)
        finally:
            self._lock.unlock()

    def queryAllUnsuccessJob(self,page=-1,per=50):
        self._cursor.execute("SELECT COUNT(*) from jobTable WHERE status LIKE 'KILLED' OR status LIKE 'FAILED'")
        r=self._cursor.fetchone()
        count = r[0]

        # just return count.
        if (page==-1):
            return count

        # watch out, bugs come here.
        pages = (count + per - 1) / per;
        limit = per
        if (page == (pages - 1)): # last page.
            limit = count - page * per;
        self._cursor.execute("SELECT * from jobTable WHERE status LIKE 'KILLED' OR status LIKE 'FAILED' LIMIT ? OFFSET ?",
                             (limit,count - page*per - per))
        result=[]
        for r in self._cursor:
            result.append(r)
        # TODO(dirlt): reverse in SQL.
        result=result[::-1]

        # return result.
        return (result,count)

    def queryDeletionImpactedJob(self,jobName):
        try:
            self._lock.lock()
            self._cursor.execute("SELECT * from jobTable WHERE dep LIKE ?",('%'+jobName+'%',))
            result=[]
            for r in self._cursor:
                result.append(r)
            return result
        finally:
            self._lock.unlock()

    def updateJobStatus(self,jobName,status):
        try:
            # check whether the job exists.
            self._lock.lock()
            if(not self.isJobExisted(jobName)):
                return 'job(%s) is not existed'%(jobName)
            SQL="UPDATE jobTable SET status=? WHERE jobName=?"
            self._cursor.execute(SQL,(status,
                                      jobName))
            self._conn.commit()
            return 'OK'
        finally:
            self._lock.unlock()

    def incJobFailedTime(self,jobName):
        try:
            # check whether the job exists.
            self._lock.lock()
            if(not self.isJobExisted(jobName)):
                return 'job(%s) is not existed'%(jobName)
            SQL = "SELECT failedTime from jobTable WHERE jobName=?"
            self._cursor.execute(SQL,(jobName,))
            failedTime = 0
            for r in self._cursor:
                if not r[0]:
                    failedTime = 0
                else:
                    failedTime = r[0]
                break
            failedTime+=1
            SQL = "UPDATE jobTable SET failedTime=? WHERE jobName=?"
            self._cursor.execute(SQL,(failedTime,jobName))
            self._conn.commit()
            return 'OK'
        finally:
            self._lock.unlock()

    def updateJobStartTime(self,jobName,ts):
        try:
            # check whether the job exists.
            self._lock.lock()
            if(not self.isJobExisted(jobName)):
                return 'job(%s) is not existed'%(jobName)
            SQL="UPDATE jobTable SET startTime=? WHERE jobName=?"
            self._cursor.execute(SQL,(ts,
                                      jobName))
            self._conn.commit()
            return 'OK'
        finally:
            self._lock.unlock()

    def updateJobEndTime(self,jobName,ts):
        try:
            # check whether the job exists.
            self._lock.lock()
            if(not self.isJobExisted(jobName)):
                return 'job(%s) is not existed'%(jobName)
            SQL="UPDATE jobTable SET endTime=? WHERE jobName=?"
            self._cursor.execute(SQL,(ts,
                                      jobName))
            self._conn.commit()
            return 'OK'
        finally:
            self._lock.unlock()

    def updateJobDescription(self,jobName,description):
        try:
            # check whether the job exists.
            self._lock.lock()
            if(not self.isJobExisted(jobName)):
                return 'job(%s) is not existed'%(jobName)
            SQL="UPDATE jobTable SET description=? WHERE jobName=?"
            self._cursor.execute(SQL,(description,
                                      jobName))
            self._conn.commit()
            return 'OK'
        finally:
            self._lock.unlock()

    def queryNotDoneJob(self):
        try:
            self._lock.lock()
            # RUNNINg or WAITING
            # KILLED, FAILED, SUCCESS.
            self._cursor.execute("SELECT * from jobTable WHERE status == 'RUNNING' or status=='WAITING'")
            result=[]
            for r in self._cursor:
                result.append(r)
            return result
        finally:
            self._lock.unlock()

    def queryNotDoneJobObject(self):
        result=self.queryNotDoneJob()
        jobs=[]
        for r in result:
            job=Job.readFromDB(r)
            jobs.append(job)
        return jobs

    def queryJob(self,jobName):
        try:
            self._lock.lock()
            if(not self.isJobExisted(jobName)):
                return ('job(%s) is not existed'%(jobName),None)
            self._cursor.execute("SELECT * from jobTable WHERE jobName=?",(jobName,))
            for r in self._cursor:
                return ('OK',r)
        finally:
            self._lock.unlock()

    def queryJobObject(self,jobName):
        (code,r)=self.queryJob(jobName)
        if(r):
            job=Job.readFromDB(r)
            return (code,job)
        return (code,None)

    def queryWaitingJob(self):
        try:
            self._lock.lock()
            self._cursor.execute("SELECT * from jobTable WHERE status == 'WAITING'")
            result=[]
            for r in self._cursor:
                result.append(r)
            return result
        finally:
            self._lock.unlock()

    def queryWaitingJobObject(self):
        result=self.queryWaitingJob()
        jobs=[]
        for r in result:
            job=Job.readFromDB(r)
            jobs.append(job)
        return jobs
