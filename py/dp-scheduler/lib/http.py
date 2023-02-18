#!/usr/bin/env python
#coding:utf-8
#Copyright (C) dirlt

import os
from wsgiref.validate import validator
from wsgiref.simple_server import make_server
from cgi import escape
from urlparse import parse_qs
import urllib
import urllib2
import sys
import json
from xml.sax.saxutils import escape
from util import exceptionToString,getLogger
from job import Job,convertDateTimeToTimeStamp,convertTimeStampToDateTime
#from db import JobDataBase
from mysqldb import JobDataBase
import time

class HTTPServer(object):
    def __init__(self,env,admin):
        self._env=env
        self._admin=admin # admin mode.
        self._logger=env['_logger']
        self._db=env['_db'].instance()
        self.kStatus = '200 OK' # HTTP Status
        self.kAccepted=('submit','delete',
                        # ralter is request alter.
                        # galter is GET alter.
                        'alter','ralter','galter',
                        'fstart','restart',
                        'success','kill',
                        'view','dep',
                        'reportOn','reportOff',
                        'retryOn','retryOff',
                        # view stdout and stderr log.
                        'stdout','stderr','info',
                        'health')
        self.kFields=('jobName','command','dep','schedTime','status','force','startTime','endTime','description')
        self._host=env['nsched.http-host']
        self._port=int(env['nsched.http-port'])
        self._refresh_interval=int(env['nsched.http-page-refresh-interval'])

    def parseArgs(self,query):
        refresh = self._refresh_interval
        if('refresh' in query):
            refresh = int(query['refresh'][0])
        pattern=''
        if('pattern' in query):
            pattern = query['pattern'][0]
        rpattern=urllib.quote(pattern)
        page=0
        if('page' in query):
            page = int(query['page'][0])
        return (refresh,pattern,rpattern,page)

    def stdout(self,env):
        query=parse_qs(env['QUERY_STRING'])
        jobName=query['id'][0] # first item.
        size=int(query['size'][0])
        outlog = os.path.join(self._env['nsched.log-dir'],jobName+'.stdout')
        d=''
        thres=int(self._env['nsched.max-fetch-log-size'])
        if(size>thres):
            size=thres
        if(os.path.isfile(outlog)):
            f=open(outlog)
            d=f.read()
            d=d[-size:]
        return ([('Content-type','text/plain')],d)

    def stderr(self,env):
        query=parse_qs(env['QUERY_STRING'])
        jobName=query['id'][0] # first item.
        size=int(query['size'][0])
        errlog = os.path.join(self._env['nsched.log-dir'],jobName+'.stderr')
        d=''
        thres=int(self._env['nsched.max-fetch-log-size'])
        if(size>thres):
            size=thres
        if(os.path.isfile(errlog)):
            f=open(errlog)
            d=f.read()
            d=d[-size:]
        return ([('Content-type','text/plain')],d)

    def refreshText(self,env,msg):
        query=parse_qs(env['QUERY_STRING'])
        msg = str(msg)
        if('xrefresh' in query and
           msg == 'OK'):
            xrefresh=int(query['xrefresh'][0])
            (refresh,pattern,rpattern,page)=self.parseArgs(query)
            page='<html><head><meta http-equiv="refresh" content="%(xrefresh)d;url=/view?pattern=%(rpattern)s&page=%(page)d&refresh=%(refresh)d"></head><body>%(msg)s</body></html>'%(locals())
            return ([('Content-type','text/html')],page)
        return ([('Content-type','text/plain')],msg)

    def logic(self,environ,start_response):
        # we just need to return a string
        try:
            content=self.handleRequest(environ)
            # return tuple, (type,text)
            (type,text)=content
            start_response(self.kStatus,type)
            return [text,]
        # caught exception.
        except Exception,_:
            es='exception caught:\n%s'%(exceptionToString())
            (type,text)=self.refreshText(environ,es)
            start_response(self.kStatus,type)
            return [text,]

    def run(self):
        self._db=self._db.clone() # recreate one.
        # because sliqte object not allowd create in one thread and used in another one.
        def logic(environ,start_response):
            return self.logic(environ,start_response)
        #vlogic=validator(logic)
        #self._httpd = make_server(self._host, self._port, vlogic)
        self._httpd = make_server(self._host, self._port, logic)
        self._logger.debug("Listening on port %d...."%(self._port))
        self._httpd.serve_forever()

    def stop(self):
        self._logger.debug('shutdown httpd...')
        self._httpd.shutdown()

    def handleRequest(self,environ):
        # http://webpython.codepoint.net/wsgi_tutorial
        # REQUEST_METHOD = 'GET'/'POST'
        # PATH_INFO
        # CONTENT_LENGTH
        # QUERY_STRING using cgi.parse_qs
        # wsgi.input

        # check path.
        pi=environ['PATH_INFO'][1:] # eliminate '/'
        pi = pi or 'view' # default value.
        if(not pi in self.kAccepted):
            s="unknown path(%s)"%(pi)
            return ([('Content-type','text/plain')],s)
        self._logger.debug('PATH_INFO = %s'%(pi))
        # !!! self.__getattr__ doesn't work?.
        return self.__getattribute__(pi)(environ)
        # return self.__getattr__(pi)(environ)

    def submit(self,env):
        length=env['CONTENT_LENGTH']
        input=env['wsgi.input']
        data=input.read(int(length))
        js=json.loads(data)
        if(isinstance(js,dict)):
            js=(js,) # make list.
        # for batch submit.
        page=''
        for j in js:
            job=Job.readin(j)
            msg=self._db.addJob(job)
            if(msg!='OK'):
                page += msg + '\n'
        if(not page):
            page = 'OK'
        return self.refreshText(env,page)

    def retryOn(self,env):
        page = 'OK'
        os.remove(self._env['nsched.no-retry-file'])
        return self.refreshText(env,page)

    def retryOff(self,env):
        page = 'OK'
        open(self._env['nsched.no-retry-file'],'w')
        return self.refreshText(env,page)

    def reportOn(self,env):
        page = 'OK'
        os.remove(self._env['nsched.notify.no-report-file'])
        return self.refreshText(env,page)

    def reportOff(self,env):
        page = 'OK'
        open(self._env['nsched.notify.no-report-file'],'w')
        return self.refreshText(env,page)

    def delete(self,env):
        query=parse_qs(env['QUERY_STRING'])
        jobName=query['id'][0] # first item.
        msg=self._db.deleteJob(jobName)
        return self.refreshText(env,msg)

    def getJobInJson(self,jobName):
        fields = self.kFields + ('jobId','failedTime')
        (msg,result)=self._db.queryJob(jobName)
        sub = {}
        if msg=='OK':
            i = 0
            for r in result:
                if r:
                    sub[fields[i]]=r
                i+=1
        return sub

    def info(self,env):
        query = parse_qs(env['QUERY_STRING'])
        jobNames = query['id']
        d = {}
        for jobName in jobNames:
            d[jobName]=getJobInJson(jobName)
        return self.refreshText(env,json.dumps(d))

    def alter(self,env):
        length=env['CONTENT_LENGTH']
        input=env['wsgi.input']
        data=input.read(int(length))
        js=json.loads(data)
        if(isinstance(js,dict)):
            js=(js,) # make list.
        # for batch alter.
        page=''
        for j in js:
            job=Job.readin(j)
            msg=self._db.updateJob(job)
            if(msg!='OK'):
                page+=msg+'\n'
        if(not page):
            page='OK'
        return self.refreshText(env,page)

    def fstart(self,env):
        query=parse_qs(env['QUERY_STRING'])
        jobName=query['id'][0] # first item.
        msg=self._db.forceStartJob(jobName)
        return self.refreshText(env,msg)

    def restart(self,env):
        query=parse_qs(env['QUERY_STRING'])
        jobName=query['id'][0] # first item.
        msg = self._db.restartJob(jobName)
        return self.refreshText(env,msg)

    def success(self,env):
        query=parse_qs(env['QUERY_STRING'])
        jobName=query['id'][0] # first item.
        msg = self._db.successJob(jobName)
        return self.refreshText(env,msg)

    def kill(self,env):
        query=parse_qs(env['QUERY_STRING'])
        jobName=query['id'][0] # first item.
        msg = self._db.killJob(jobName)
        return self.refreshText(env,msg)

    def ralter(self,env):
        query=parse_qs(env['QUERY_STRING'])
        jobName=query['id'][0] # first item.
        (code,job)=self._db.queryJobObject(jobName)
        if(code!='OK'):
            return self.refreshText(env,code)
        host=os.uname()[1]
        jobName=job.jobName()
        command=job.command()
        dep=json.dumps(job.dep())
        schedTime=convertTimeStampToDateTime(job.schedTime())
        (refresh,pattern,rpattern,page)=self.parseArgs(query)
        HTML="""<html><head><title>nsched@(host)s</title></head><body>
        <hr/><h1>Alter %(jobName)s</h1>
        <form method="get"><table>
        <tr><td>jobName</td><td><input type="txt" name="id" value="%(jobName)s" readonly="readonly"/></td></tr>
        <tr><td>command</td><td><input type="txt" name="cmd" value="%(command)s"/></td></tr>
        <tr><td>dep</td><td><input type="txt" name="dep" value='%(dep)s'/></td></tr>
        <tr><td>schedTime</td><td><input type="txt" name="sched" value="%(schedTime)s"/></td></tr></table>
        <input type="hidden" name="xrefresh" value="1"/>
        <input type="hidden" name="pattern" value="%(rpattern)s"/>
        <input type="hidden" name="page" value="%(page)d"/>
        <input type="hidden" name="refresh" value="%(refresh)d"/>
        <input type="submit" value="OK" onclick="this.form.action='/galter'"/><br/>
        </form></body></html>"""
        s=HTML%(locals())
        s=s.replace('\n','')
        return ([('Content-type','text/html')],s)

    def galter(self,env):
        query=parse_qs(env['QUERY_STRING'])
        jobName=query['id'][0]
        command=query['cmd'][0]
        dep=json.loads(query['dep'][0])
        schedTime=convertDateTimeToTimeStamp(query['sched'][0])
        job=Job.readin({'jobName':jobName,
                        'dep':dep,
                        'command':command,
                        'schedTime':schedTime})
        msg=self._db.updateJob(job)
        return self.refreshText(env,msg)

    def view(self,env):
        query=parse_qs(env['QUERY_STRING'])
        (refresh,pattern,rpattern,page)=self.parseArgs(query)
        kJobNumberPerPage = 10

        # pages and search box.
        (result,all)=self._db.queryAllJob(pattern,page,kJobNumberPerPage)
        allPages = (all + kJobNumberPerPage-1)/kJobNumberPerPage
        prev=page-1
        if(prev<0):prev=0
        next=page+1
        last=allPages-1
        if(next>=last):next=last

        report = True
        reportLink = 'Off'
        reportTag = 'On'
        if os.path.exists(self._env['nsched.notify.no-report-file']):
            report = False
            reportTag = 'Off'
            reportLink = 'On'

        retry = True
        retryLink = 'Off'
        retryTag = 'On'
        if os.path.exists(self._env['nsched.no-retry-file']):
            retry = False
            retryTag = 'Off'
            retryLink = 'On'


        utilHTML=''
        utilHTML+='<table><tr><td>page index(%(all)d jobs)</td>'
        utilHTML+='<td> <a href="/view?pattern=%(rpattern)s&page=0&refresh=%(refresh)d">first</a> <td>'
        utilHTML+='<td> <a href="/view?pattern=%(rpattern)s&page=%(prev)d&refresh=%(refresh)d">prev</a> <td>'
        utilHTML+='<td> current page[%(page)d/%(allPages)d] </td>'
        utilHTML+='<td> <a href="/view?pattern=%(rpattern)s&page=%(next)d&refresh=%(refresh)d">next</a> </td>'
        utilHTML+='<td> <a href="/view?pattern=%(rpattern)s&page=%(last)d&refresh=%(refresh)d">last</a> </td>'
        #utilHTML+='<td> <a href="/view?pattern=%(rpattern)s&page=-1&refresh=%(refresh)d">all</a> </td>'
        utilHTML+='<td>report <a href="/report%(reportLink)s?xrefresh=1">%(reportTag)s</a> </td>'
        utilHTML+='<td>retry <a href="/retry%(retryLink)s?xrefresh=1">%(retryTag)s</a> </td>'
        utilHTML+='<td> <a href="/health">health</a> </td>'
        utilHTML+='</tr></table>'

        unsuccessCount = self._db.queryAllUnsuccessJob()
        successCount = self._db.queryAllJob('SUCCESS')
        waitingCount = self._db.queryAllJob('WAITING')
        runningCount = self._db.queryAllJob('RUNNING')
        failedCount = self._db.queryAllJob('FAILED')
        killedCount = self._db.queryAllJob('KILLED')


        utilHTML+="""
        <table><tr>
        <td><a href="/?pattern=UNSUCCESS&refresh=%(refresh)d">unsuccess</a>(%(unsuccessCount)d)</td>
        <td><a href="/?pattern=SUCCESS&refresh=%(refresh)d">success</a>(%(successCount)d)</td>
        <td><a href="/?pattern=WAITING&refresh=%(refresh)d">waiting</a>(%(waitingCount)d)</td>
        <td><a href="/?pattern=RUNNING&refresh=%(refresh)d">running</a>(%(runningCount)d)</td>
        <td><a href="/?pattern=FAILED&refresh=%(refresh)d">failed</a>(%(failedCount)d)</td>
        <td><a href="/?pattern=KILLED&refresh=%(refresh)d">killed</a>(%(killedCount)d)</td>
        </tr></table>
        <form method="get"><table><tr><td>search by jobname(or status)</td><td><input type="txt" name="pattern" value=""/></td>
        <td><input type="submit" value="search" onclock="this.form.action='/view'"/></td>
        </tr></table><input type="hidden" name="refresh" value="%(refresh)d"/>
        <!-- <input type="hidden" name="page" value="%(page)d"/> --></form>"""
        search=utilHTML%(locals())

        # main page.
        HTML="""<html>
        <head><meta http-equiv="refresh" content="%(refresh)d;url=/view?refresh=%(refresh)d&page=%(page)d&pattern=%(rpattern)s"/><title>nsched@%(host)s</title></head>
        <body>
        <hr/><h1>Jobs</h1>%(search)s
        <table border="1">
        %(table_header)s
        %(table_content)s
        </table>
        </body>
        </html>"""
        host=os.uname()[1]
        table_header='<tr>'
        for f in self.kFields:
            table_header+='<th>%s</th>'%(f)
        table_header+='</tr>'

        table_content=''
        for r in result:
            table_content+='<tr>'
            for i in range(len(self.kFields)):
                f=self.kFields[i]
                c=r[i]
                if(i==0):
                    rjobName=(str(c))
                    jobName=urllib.quote(rjobName)
                    s='<td>%(rjobName)s<br/><ul>'
                    # admin give ability to change job.
                    if(self._admin):
                        s+='<li><a href="/delete?id=%(jobName)s&xrefresh=1&refresh=%(refresh)d&pattern=%(rpattern)s&page=%(page)d">delete</a> / <a href="/ralter?id=%(jobName)s&refresh=%(refresh)d&pattern=%(rpattern)s&page=%(page)d">alter</a></li>'
                        s+='<li><a href="/fstart?id=%(jobName)s&xrefresh=1&refresh=%(refresh)d&pattern=%(rpattern)s&page=%(page)d">fstart</a> / <a href="/restart?id=%(jobName)s&xrefresh=1&refresh=%(refresh)d&pattern=%(rpattern)s&page=%(page)d">restart</a></li>'
                        s+='<li><a href="/success?id=%(jobName)s&xrefresh=1&refresh=%(refresh)d&pattern=%(rpattern)s&page=%(page)d">success</a> / <a href="/kill?id=%(jobName)s&xrefresh=1&refresh=%(refresh)d&pattern=%(rpattern)s&page=%(page)d">kill</a></li>'
                    # normal mode.
                    s+='<li><a href="/dep?id=%(jobName)s">jobs depend on</a></li>'
                    s+='<li>out <a href="/stdout?id=%(jobName)s&size=4096">4k</a> / <a href="/stdout?id=%(jobName)s&size=8192">8k</a> / <a href="/stdout?id=%(jobName)s&size=16384">16k</a></li>'
                    s+='<li>err  <a href="/stderr?id=%(jobName)s&size=4096">4k</a> / <a href="/stderr?id=%(jobName)s&size=8192">8k</a> / <a href="/stderr?id=%(jobName)s&size=16384">16k</a></li></ul></td>'
                    s=s%(locals())
                    table_content+=s
                else:
                    v = escape(str(c))
                    if(f in ('schedTime','startTime','endTime')):
                        v = convertTimeStampToDateTime(c)
                    table_content+='<td>%s</td>'%(v)
            table_content+='</tr>'
        s=HTML%(locals())
        s=s.replace('\n','')
        return ([('Content-type','text/html')],s)

    def dep(self,env):
        # query deletion.
        query=parse_qs(env['QUERY_STRING'])
        jobName=query['id'][0] # first item.
        result=self._db.queryDeletionImpactedJob(jobName)
        host=os.uname()[1]

        HTML="""<html>
        <title>nsched@%(host)s</title>
        <body>
        <hr/><h1>Jobs depend on %(jobName)s</h1>
        <table border="1">
        %(table_header)s
        %(table_content)s
        </table>
        </body>
        </html>"""
        table_header='<tr>'
        for f in self.kFields:
            table_header+='<th>%s</th>'%(f)
        table_header+='</tr>'

        table_content=''
        for r in result:
            table_content+='<tr>'
            for i in range(len(self.kFields)):
                f=self.kFields[i]
                c=r[i]
                if(f in ('schedTime','startTime','endTime')):
                    v=convertTimeStampToDateTime(c)
                else:
                    v=escape(str(c))
                table_content+='<td>%s</td>'%(v)
            table_content+='</tr>'

        s=HTML%(locals())
        s=s.replace('\n','')
        return ([('Content-type','text/html')],s)

    def health(self,env):
        cache = {}

        query = parse_qs(env['QUERY_STRING'])

        class HealthStatus:
            def __init__(self):
                self.normal = 0
                self.allDelay = 0
                self.specialDelay = 0
                self.delayIn2 = 0
                self.specialIn2 = 0
                self.delayIn4 = 0
                self.specialIn4 = 0
                self.delayOut4 = 0
                self.specialOut4 = 0
                self.ignore = []
                self.score = 0.0
                self.endTime = 0
                self.date = ''

        def getHealthStatus(dts):
            ts = dts
            ids = []
            while ts > (dts - 3600 * 24 * 30):
                st = time.localtime(ts)
                d = '%04d%02d%02d'%(st.tm_year,st.tm_mon,st.tm_mday)
                id = 'app_user_stat#%s'%(d)
                ids.append(id)
                ts -= 3600 * 24
            js = {}
            for id in ids:
                if not id in cache:
                    cache[id] = self.getJobInJson(id)
                js[id] = cache[id]

            stat = HealthStatus()

            for id in ids:
                if not id in js or not js[id]:
                    stat.ignore.append(id)
                    continue
                info = js[id]
                if info['status']!='SUCCESS' or not 'endTime' in info:
                    stat.ignore.append(id)
                    continue

                (_,ymd)=id.split('#')
                (y,m,d)=(ymd[0:4],ymd[4:6],ymd[6:8])
                # bound as 10:00:00
                schedTime = convertDateTimeToTimeStamp('%s-%s-%s 10:00:00'%(y,m,d))
                st = time.localtime(schedTime)

                specialDay = st.tm_wday in (0,4) # monday and friday
                delay = info['endTime'] - schedTime

                if delay < 0:
                    stat.normal += 1
                elif delay < 2 * 3600:
                    stat.delayIn2 += 1
                    if specialDay:
                        stat.specialIn2 += 1
                elif delay < 4 * 3600:
                    stat.delayIn4 += 1
                    if specialDay:
                        stat.specialIn4 += 1
                else:
                    stat.delayOut4 += 1
                    if specialDay:
                        stat.specialOut4 += 1

            cid = ids[0]
            if not cid in js or not js[cid] or js[cid]['status']!='SUCCESS' or not 'endTime' in js[cid]:
                stat.endTime = 0
            else:
                stat.endTime = js[cid]['endTime']

            stat.allDelay = stat.delayIn2 + stat.delayIn4 + stat.delayOut4
            stat.specialDelay = stat.specialIn2 + stat.specialIn4 + stat.specialOut4

            stat.score = stat.normal * 3.3
            stat.score += (stat.delayIn2 - stat.specialIn2) * 1 + stat.specialIn2 * 0
            stat.score += (stat.delayIn4 - stat.specialIn4) * 0 + stat.specialIn4 * -1
            stat.score += (stat.delayOut4 - stat.specialOut4) * -1 + stat.specialOut4 * -2
            stat.date = convertTimeStampToDateTime(dts)[0:10]
            return stat

        hst = []
        dts = time.time()

        if 'date' in query:
            date = query['date'][0]
            dts = convertDateTimeToTimeStamp(date + ' 00:00:00')

        ts = dts - 3600 * 24 * 30 # recently month.
        while ts < dts:
            ts += 3600 * 24
            hst.append(getHealthStatus(ts))
        hst = hst[::-1]

        HTML = """<html>
        <head><title>nsched@%(host)s</title></head>
        <body>
        <hr/><h1>Health</h1>%(algorithm)s<table border="1">
        %(table_header)s
        %(table_content)s
        </table>
        </body>
        </html>"""

        algorithm = """<pre>
score = normal * 3.3 +
        (delay[0-2] - delay[0-2]:mf) * 1 + delay[0-2]:mf * 0 +
        (delay[2-4] - delay[2-4]:mf) * 0 + delay[2-4]:mf * -1 +
        (delay[4+] - delay[4+]:mf) * -1 + delay[4+]:mf * -2
mf = monday or friday
        </pre>"""

        host = os.uname()[1]
        fields = ('date','score','normal','delay/mf','delay[0-2]/mf','delay[2-4]/mf','delay[4+]/mf','ignore','endTime')
        table_header = '<tr>'
        for f in fields:
            table_header += '<th>%s</th>'%(f)
        table_header += '</tr>'

        table_content = ''
        for h in hst:
            ignore = len(h.ignore)
            table_content+='<tr>'
            table_content+='<td>%s</td><td>%.2f</td><td>%d</td><td>%d/%d</td><td>%d/%d</td><td>%d/%d</td><td>%d/%d</td><td>%d</td><td>%s</td>'%(
                h.date,h.score,
                h.normal,h.allDelay,h.specialDelay,
                h.delayIn2,h.specialIn2,
                h.delayIn4,h.specialIn4,
                h.delayOut4,h.specialOut4,
                ignore,convertTimeStampToDateTime(h.endTime))
            table_content+='</tr>'

        s = HTML%(locals())
        #s = s.replace('\n','')

        return ([('Content-type','text/html')],s)

