#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

import json
import time
import os

from job import Job, convertDateTimeToTimeStamp, convertTimeStampToDateTime
from task import makeJobRequest
from util import getLogger, nsched_notify
import urllib
import requests
import redis
import commands


class EasyMailHandler:
    def __init__(self, env):
        self._env = env
        self._last = 0
        self._lagReportInterval = int(self._env['nsched.notify.interval'])
        self._smshost = self._env['nsched.sms-alert.host']
        self._smsport = int(self._env['nsched.sms-alert.port'])

    def mail(self, jobName):
        now = time.time()
        if (now > (self._last + self._lagReportInterval) and
                not os.path.exists(self._env['nsched.notify.no-report-file'])):
            host = os.uname()[1]
            subject = "[nsched@%s]RUN JOB LAGGED '%s'" % (host, jobName)
            text = 'RT'
            nsched_notify(self._env, subject, text)
            self._last = now
            rightnow = time.strftime('%Y-%m-%d %H:%M:%S')
            info = {
                'type': 'LAG WARN',
                'desc': 'Run job delay',
                'host': host,
                'itemkey': rightnow,
                'msg': jobName
            }
            headers = {'content-type': 'application/json'}
            try:
                r = requests.post("http://%s:%s/sendsms/json/" % (self._smshost, self._smsport), data=json.dumps(info), headers=headers)
            except Exception:
                subject = "[sms send error@%s]RUN JOB LAGGED '%s'" % (host, jobName)
                nsched_notify(self._env, subject, text)


class Coord(object):
    def __init__(self, env):
        self._env = env
        self._logger = env['_logger']
        self._db = env['_db'].instance()
        self._task = env['_task']
        self._ctask = env['_ctask']
        self._snapshot = {}
        self._redisHost = env['nsched.redis-host']
        self._redis = redis.Redis(host=self._redisHost, db=1)
        self._exit = False

    def parseJobStatus(self, job, dep, v):
        def closure():
            status = self._db.queryJobStatus(dep)
            if (status != 'SUCCESS'):
                desc = 'job(%s) dep(%s) not done' % (job.jobName(), dep)
                self._logger.debug(desc)
                return (False, desc)
            self._logger.debug('job(%s) dep(%s) done' % (job.jobName(), dep))
            return (True, None)

        return closure

    def parseFileReady(self, job, path):
        def closure():
            code = os.path.isfile(path)
            desc = "job(%s) file-ready condition(%s) path=%s" % (job.jobName(), code, path)
            self._logger.debug(desc)
            return (code, desc)

        return closure

    def parseDepR(self, job, dep):
        (opcode, struct) = (dep[0], dep[1:])
        operands = []
        for s in struct:
            if (isinstance(s, list)):
                # recursive parse.
                operands.append(self.parseDepR(job, s))
                continue
            assert (isinstance(s, dict))
            operand = None
            for k in s.keys():
                v = s[k]
                if (k == 'file-ready'):
                    operand = self.parseFileReady(job, v)
                elif (k.startswith('job-status')):
                    # job-status@<jobName>
                    x = k.split('@')[1]
                    operand = self.parseJobStatus(job, x, v)
                else:
                    self._logger.warning('unknown key(%s), ignore it.' % (k))
                if (operand):
                    operands.append(operand)

        def closure():
            op = opcode
            if (op not in ('and', 'or',)):
                op = 'and'  # default.
            if (op == 'and'):
                for o in operands:
                    (code, desc) = o()
                    if (code == False):
                        return (False, desc)
                return True, None
            elif (op == 'or'):
                for o in operands:
                    (code, desc) = o()
                    if (code == True):
                        return True, None
                return False, desc

        return closure

    def parseDep(self, job):
        dep = job.dep()
        if (not dep):
            def true():
                return (True, None)

            return true

        if (isinstance(dep, dict)):
            if ('lagtime' in dep):
                lagTime = int(dep['lagtime'])
                job.lagTime = lagTime
            dep = dep['rest']
        closure = self.parseDepR(job, dep)
        return closure

    def setup(self):
        jobs = self._db.queryNotDoneJobObject()
        for job in jobs:
            jobName = job.jobName()
            # for local job, it must be killed.
            status = 'KILLED'

            # action.
            if (status == 'KILLED'):
                self._logger.debug("update job(%s) 'KILLED'" % (job.jobName()))
                self._db.updateJobStatus(job.jobName(), 'KILLED')

    def appendWaitingJob(self, new, job, condition):
        item = {'job': job,
                'cond': condition}
        new[job.jobName()] = item

    def mergeWithSnapshot(self, jobs):
        snapshot = self._snapshot
        # make index.
        index = {}
        for job in jobs:
            index[job.jobName()] = job

        # merge.
        new = {}
        for x in snapshot:
            if (x in index):
                # check whether same.
                if (snapshot[x]['job'].notChanged(index[x])):
                    new[x] = snapshot[x]
                    continue

                # recreate condition because alter.
                condition = self.parseDep(index[x])
                self.appendWaitingJob(new, index[x], condition)

        for x in index:
            if (not x in snapshot):
                # create condition because sumbit.
                condition = self.parseDep(index[x])
                self.appendWaitingJob(new, index[x], condition)

        # assignment.
        self._snapshot = new

    def start(self):
        self._exit = False
        self._task.start()
        self._ctask.start()

    def runJob(self, job):
        self._logger.info('start job(%s) command(%s)' % (job.jobName(),
                                                         job.command()))
        self._db.updateJobStatus(job.jobName(), 'RUNNING')
        self._db.updateJobStartTime(job.jobName(), time.time())
        # self._db.updateJobDescription(job.jobName(),'')
        self._task.putRequest(makeJobRequest(job.jobName(),
                                             job.command(),
                                             self._env))

    def run(self):
        while True:
            try:
                self._run()
            except Exception, e:
                self._logger.debug("run error=>%s", e)
                pass
            if self._exit:
                break

    def _run(self):
        loop_interval = int(self._env['nsched.coord-loop-interval'])  # in seconds.
        last = -1
        while (True):
            if (self._exit):
                break
            now = time.time()
            if (now <= (last + loop_interval)):
                time.sleep((last + loop_interval) - now)

            self._redis.set('istillalive', '', ex=self._env['nsched.sms-alert.expire'])
            self._logger.debug('loop again %d, send heart beat to redis' % (time.time()))
            jobs = self._db.queryWaitingJobObject()
            # merge with snapshot.
            self.mergeWithSnapshot(jobs)
            # check condition
            torun = []
            for x in self._snapshot:
                try:
                    job = self._snapshot[x]['job']
                    if (self._db.isJobForcedStart(job.jobName())):
                        self.runJob(job)
                        torun.append(job.jobName())
                        continue
                    if (job.schedTime() > time.time()):
                        (code, desc) = (False, 'job(%s) not at schedule time(%s)' % (job.jobName(),
                                                                                     convertTimeStampToDateTime(
                                                                                         job.schedTime())))
                    else:
                        closure = self._snapshot[x]['cond']
                        (code, desc) = closure()

                    if (code):
                        self.runJob(job)
                        torun.append(job.jobName())
                    else:
                        # optimization for not update description too frequent.
                        if (job.blockDesc() != desc):
                            self._logger.debug("not saved update db for job description,desc'%s', now '%s'",
                                               job.blockDesc(), desc)
                            self._db.updateJobDescription(job.jobName(), desc)
                            job.setBlockDesc(desc)

                            # if the job has been lagged too much, mail me.
                        if (hasattr(job, 'lagTime')):
                            lagTime = job.lagTime
                            if ((job.schedTime() + lagTime) < time.time()):
                                if (not hasattr(job, 'handler')):
                                    job.handler = EasyMailHandler(self._env)

                                def makeCallable(j):
                                    def _callable():
                                        j.handler.mail(j.jobName())

                                    return _callable

                                self._logger.debug('job(%s) lagged' % (job.jobName()))
                                self._ctask.putRequest(makeCallable(job))
                except Exception, e:
                    self._logger.debug(e)

            for x in torun:
                del self._snapshot[x]
            last = time.time()

    def stop(self):
        self._task.stop()
        self._ctask.stop()
        self._exit = True

