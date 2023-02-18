#!/usr/bin/env python
#coding:utf-8

import MySQLdb
import json
import threading

from job import Job,convertDateTimeToTimeStamp,convertTimeStampToDateTime
#from util import MutexThreadLock,getLogger
kMaxSchedTime = convertDateTimeToTimeStamp('3000-01-01 00:00:00')
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
    def __init__(self,env):
        self._env=env
        self._logger=env['_logger']
        self._dbhost=env['nsched.db-host']
        self._dbname=env['nsched.db-name']
        #self._conn=MySQLdb.connect(host="localhost",port=3306,user="root",passwd="Mysqldo0",db="bright")
        self._conn=MySQLdb.connect(host=self._dbhost,port=3306,user="nsched",passwd="root@dpm",db=self._dbname)
        self._conn.ping(True)
        self._conn.autocommit(True)
        self._cursor=self._conn.cursor()

    def close(self):
        self._conn.close()

    def clone(self):
        return JobDataBase(self._env)

    def dropTable(self):
        SQL="DROP TABLE IF EXISTS jobTable";
        self._cursor.execute(SQL)

    def createTable(self):
        schema="""(
        jobName varchar(100) PRIMARY KEY,
        command text,
        dep text,
        schedTime integer,
        status text,
        isForce text,
        startTime integer,
        endTime integer,
        description text,
        jobId text,
        failedTime integer
        )"""
        SQL="CREATE TABLE IF NOT EXISTS jobTable %s"%(schema)
        self._cursor.execute(SQL)

    def isJobExisted(self,jobName):
        SQL="SELECT jobName FROM jobTable WHERE jobName=%s"
        self._cursor.execute(SQL,(jobName,))
        return self._cursor.fetchone()

    def addJob(self,job):
        # check whether the job exists.
        if(self.isJobExisted(job.jobName())):
            return 'job(%s) is existed'%(job.jobName())

        # workaround.
        # if schedTime is too much
        # I think our intention is to let job start manually.
        status = 'WAITING'
        if(job.schedTime() >= kMaxSchedTime):
            job.setSchedTime(0)
            status = 'KILLED'
        print status

        try:
            SQL="INSERT INTO jobTable values(%s,%s,%s,%s,%s,'false',0,0,'','',0)"
            self._cursor.execute(SQL,(job.jobName(),
                                      job.command(),
                                      json.dumps(job.dep()),
                                      job.schedTime(),
                                      status))
            self._conn.commit()
            return 'OK'
        except MySQLdb.Error,e:
            self._conn.rollback()
            return "Add Job %s Error %d: %s" %(job.jobName(),e.args[0],e.args[1])

    def queryJobStatus(self,jobName):
        # SUCCESS
        # KILLED
        # WAITING
        # RUNNING
        # NONE->FAILED.
        # NONE WILL NOT STORED IN DB.
        SQL="SELECT status FROM jobTable WHERE jobName=%s"
        self._cursor.execute(SQL,(jobName,))
        for r in self._cursor:
            return r[0]
        return ''

    def _updateNotRunningJob(self,jobName,sql,param,action=''):
        '''sql ---sql string maybe have '%s' insert
           param ---sequence, parameters in sql
           action --- update action like Delete/Update/ForceRestart...
        '''
        # whether running.
        status=self.queryJobStatus(jobName)
        if(not status):
            return 'job(%s) is not existed'%(jobName)
        elif(status == 'RUNNING'):
            return 'job(%s) is running'%(jobName)

        try:
            self._cursor.execute(sql,param)
            self._conn.commit()
            return 'OK'
        except MySQLdb.Error,e:
            self._conn.rollback()
            return "%s %s Error %d: %s" %(action,jobName,e.args[0],e.args[1])

    def deleteJob(self,jobName):
        sql ="DELETE FROM jobTable WHERE jobName=%s"
        param = (jobName,)
        action = "Delete"
        return self._updateNotRunningJob(jobName,sql,param,action)

    def updateJob(self,job):
        sql="UPDATE jobTable SET command=%s, dep=%s, schedTime=%s WHERE jobName=%s"
        param = (job.command(),
                 json.dumps(job.dep()),
                 job.schedTime(),
                 job.jobName())
        action = "Update"
        return self._updateNotRunningJob(job.jobName(),sql,param,action)

    def forceStartJob(self,jobName): ## TODO : Should change JobStatus???
        sql="UPDATE jobTable SET isForce='true' WHERE jobName=%s"
        param =(jobName,)
        action = "ForceStart"
        return self._updateNotRunningJob(jobName,sql,param,action)

    def isJobForcedStart(self,jobName):
        SQL="SELECT isForce from jobTable WHERE jobName=%s"
        self._cursor.execute(SQL,(jobName,))
        row=self._cursor.fetchone()
        return None!=row and row[0] == 'true'  #job exist and isForce true

    def restartJob(self,jobName):
        sql="UPDATE jobTable SET status='WAITING', isForce='false', startTime=0, endTime=0 WHERE jobName=%s"
        param=(jobName,)
        action = "Restart"
        return self._updateNotRunningJob(jobName,sql,param,action)

    def successJob(self,jobName):
        sql="UPDATE jobTable SET status='SUCCESS', isForce='false', startTime=0, endTime=0 WHERE jobName=%s"
        param=(jobName,)
        action = "Success"
        return self._updateNotRunningJob(jobName,sql,param,action)

    def killJob(self,jobName):
        sql="UPDATE jobTable SET status='KILLED', isForce='false', startTime=0, endTime=0 WHERE jobName=%s"
        param=(jobName,)
        action = "Kill"
        return self._updateNotRunningJob(jobName,sql,param,action)

    def incJobFailedTime(self,jobName):
        # check whether the job exists.
        if(not self.isJobExisted(jobName)):
            return 'job(%s) is not existed'%(jobName)
        SQL = "SELECT failedTime from jobTable WHERE jobName=%s"
        self._cursor.execute(SQL,(jobName,))
        failedTime = 0
        for r in self._cursor:
            if not r[0]:
                failedTime = 0
            else:
                failedTime = r[0]
            break
        failedTime+=1
        try:
            SQL = "UPDATE jobTable SET failedTime=%s WHERE jobName=%s"
            self._cursor.execute(SQL,(failedTime,jobName))
            self._conn.commit()
            return 'OK'
        except MySQLdb.Error,e:
            self._conn.rollback()
            return "IncJobFailedTime Error %d: %s" %(e.args[0],e.args[1])

    def _updateExistJob(self,jobName,sql,param,action):
        if(not self.isJobExisted(jobName)):
            return "job(%s) is not existed"%(jobName)
        try :
            self._cursor.execute(sql,param)
            self._conn.commit()
            return 'OK'
        except MySQLdb.Error,e:
            self._conn.rollback()
            return "%s %s Error %d: %s" %(action,jobName,e.args[0],e.args[1])

    def updateJobStatus(self,jobName,status):
        sql="UPDATE jobTable SET status=%s WHERE jobName=%s"
        param=(status,jobName)
        return self._updateExistJob(jobName,sql,param,"UpdateJobStatus")

    def updateJobStartTime(self,jobName,ts):
        sql="UPDATE jobTable SET startTime=%s WHERE jobName=%s"
        param=(ts,jobName)
        return self._updateExistJob(jobName,sql,param,"UpdateJobStartTime")

    def updateJobEndTime(self,jobName,ts):
        sql="UPDATE jobTable SET endTime=%s WHERE jobName=%s"
        param=(ts,jobName)
        return self._updateExistJob(jobName,sql,param,"UpdateJobEndTime")

    def updateJobDescription(self,jobName,description):
        sql="UPDATE jobTable SET description=%s WHERE jobName=%s"
        param=(description,jobName)
        return self._updateExistJob(jobName,sql,param,"UpdateJobDescription")

    def queryDeletionImpactedJob(self,jobName):
        self._cursor.execute("SELECT * from jobTable WHERE dep LIKE %s ORDER BY schedTime desc,jobName",('%'+jobName+'%',))
        result=[]
        for r in self._cursor:
            result.append(r)
        return result

    def queryNotDoneJob(self):
        # RUNNING or WAITING
        # KILLED, FAILED, SUCCESS.
        self._cursor.execute("SELECT * from jobTable WHERE status = 'RUNNING' or status = 'WAITING' ORDER BY schedTime desc,jobName")
        result=[]
        for r in self._cursor:
            result.append(r)
        return result

    def queryNotDoneJobObject(self):
        result=self.queryNotDoneJob()
        jobs=[]
        for r in result:
            job=Job.readFromDB(r)
            jobs.append(job)
        return jobs

    def queryJob(self,jobName):
        self._cursor.execute("SELECT * from jobTable WHERE jobName=%s ORDER BY schedTime desc,jobName",(jobName,))
        r=self._cursor.fetchone()
        if(not r):
            return ('job(%s) is not existed'%(jobName),None)
        else:
            return ('OK',r)

    def queryJobObject(self,jobName):
        (code,r)=self.queryJob(jobName)
        if(r):
            job=Job.readFromDB(r)
            return (code,job)
        else:
            return (code,None)

    def queryWaitingJob(self):
        self._cursor.execute("SELECT * from jobTable WHERE status = 'WAITING' ORDER BY schedTime desc,jobName")
        result=[]
        for r in self._cursor:
            result.append(r)
        return result

    def queryWaitingJobObject(self):
        result=self.queryWaitingJob()
        jobs=[]
        for r in result:
            job=Job.readFromDB(r)
            jobs.append(job)
        return jobs

    def queryAllUnsuccessJob(self,page=-1,per=50):
        return self.queryAllJob('UNSUCCESS',page ,per)

    def queryAllJob(self,pattern='',page=-1,per=50):
         #self._logger.info(self._conn.thread_id())
         # if pattern are followings, we search by status.
         field = 'jobName'
         if(pattern in ('RUNNING','KILLED','FAILED','SUCCESS','WAITING')):
             field = 'status'

         # ugly...
         if(not pattern):
             self._cursor.execute("SELECT COUNT(*) from jobTable")
         elif (pattern == 'UNSUCCESS'):
             self._cursor.execute("SELECT COUNT(*) from jobTable WHERE status LIKE 'KILLED' OR status LIKE 'FAILED'")
         else:#param contains char ' , need use % and \' ,as follows , wtf
             self._cursor.execute("SELECT COUNT(*) from jobTable WHERE  %s LIKE %s"%(field,'\'%'+pattern+'%\''))

         r=self._cursor.fetchone()
         count = r[0]

         # just return count.
         if (page<0):
             return count
         if(count == 0):#short path
             return ([],count)

         limit=per
         offset=per*page
         if(not pattern):
             self._cursor.execute("SELECT * from jobTable ORDER BY schedTime desc,jobName LIMIT %s OFFSET %s",(limit,offset) )
         elif (pattern == 'UNSUCCESS'):
             self._cursor.execute("SELECT * from jobTable WHERE status LIKE 'KILLED' OR status LIKE 'FAILED' \
                    ORDER BY schedTime desc,jobName  LIMIT %s OFFSET %s",(limit,offset))
         else:
             self._cursor.execute("SELECT * from jobTable WHERE %s LIKE %s ORDER BY schedTime desc,jobName LIMIT %s OFFSET %s"\
                     %(field,'\'%'+pattern+'%\'',limit,offset))
         result=[]
         for r in self._cursor:
             result.append(r)
         # reverse in SQL.
         #result=result[::-1]

         # return result.
         return (result,count)

if __name__=="__main__" :
    env = {}
    env['_logger']=''
    env['nsched.db-host']=''
    env['nsched.db-name']=''

    db=JobDataBase(env)
    db.createTable()

    pool=JobDataBasePool(db)
    dbins=pool.instance()
    job=Job()
    jobName='TestMR#1'
    job.setJobName(jobName)
    job.setCommand('cat nothing')
    job.setDep(["and",{"file-ready":"/tmp/_SUCCESS"}])
    print dbins.addJob(job)
    #print dbins.updateJobStatus(jobName+"what","FAILED")
    #print dbins.incJobFailedTime(jobName)
    #print dbins.queryDeletionImpactedJob(jobName)
    ##print dbins.queryNotDoneJobObject()
    #print dbins.queryJobObject(jobName)
    #job.setStatus("RUNNING")
    job.setCommand('cat nothing at all ')
    print dbins.updateJobStatus(jobName,"RUNNING")
    print dbins.successJob(jobName)
    print dbins.updateJob(job)
    print dbins.updateJobStatus(jobName,"FAILED")
    #print dbins.killJob(jobName)
    print dbins.deleteJob(jobName)
    #print
    #print dbins.queryAllJob('UNSUCCESS',0)
