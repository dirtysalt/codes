#!/usr/bin/env python
#coding:utf-8
#Copyright (C) dirlt

import web

urls = ('/upload', 'upload',
        '/.*', 'home')

app = web.application(urls, globals())

class home:
    def GET(self):
        return """<html><head></head><body>
<form method="POST" enctype="multipart/form-data" action="/upload">
<input type="file" name="myfile" />
<br/>
<input type="submit" />
</form>
</body></html>"""

import cgi
class upload:
    def POST(self):
        s = ''
        winput = web.input()
        for k in list(winput.keys()):
            s += '<li>%s = %s</li>' % (k, cgi.escape(str(winput[k])))
        ctx_s = ''
        for k in list(web.ctx.keys()):
            ctx_s += '<li>%s = %s</li>' % (k, cgi.escape(str(web.ctx[k])))
        env_s = ''
        for k in list(web.ctx.environ.keys()):
            env_s += '<li>%s = %s</li>' % (k, cgi.escape(str(web.ctx.environ[k])))
        html = """<html><body><p>web input<br/><ul>%s</ul></p>
        <p>web ctx<br/><ul>%s</ul></p>
        <p>web ctx environ<br/><ul>%s</ul></p></body></html>""" % (s, ctx_s, env_s)
        return html

if __name__ == "__main__":
   app.run()
