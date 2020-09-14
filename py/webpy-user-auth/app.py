#!/usr/bin/env python
#coding:utf-8
#Copyright (C) dirlt

import web
import traceback

urls = (
    '/hello', 'Hello',
    '/', 'Index',
    '/index', 'Index',
    '/login', 'Login',
    '/logout', 'Logout',
)

web.config.debug = True
web.config.session_parameters['cookie_name'] = 'webpy_session_id'
web.config.session_parameters['cookie_domain'] = None
web.config.session_parameters['timeout'] = 3600 # 改小观察session失效效果.
web.config.session_parameters['ignore_expiry'] = True
web.config.session_parameters['ignore_change_ip'] = True
web.config.session_parameters['secret_key'] = 'fLjUfxqXtfNoIldA0A0J'
web.config.session_parameters['expired_message'] = 'Session expired'

app = web.application(urls, globals())
# db = web.database(dbn = 'mysql', db = 'test', user ='root', pw = '123456')
db = web.database(dbn = 'mysql', db = 'test', user = 'root', pw = 'uvw123')
render = web.template.render('templates/')

if web.config.get('_session') is None:
    session = web.session.Session(app, web.session.DBStore(db, 'sessions'),
                                  initializer={'login': 0})
    web.config._session = session
else:
    session = web.config._session

class Hello:
    def GET(self):
        i = web.input(name = [])
        name = i.name[0] if len(i.name) != 0 else None
        return render.hello(name)

def check_login(f):
    def wf(*args, **kwargs):
        if session.login == 0: return render.login()
        return f(*args, **kwargs)
    return wf

class Index:
    @check_login
    def GET(self):
        cookies = web.cookies(tag = 'unknown')
        return 'welcome, user = {}, privilege = {}, tag = {}'.format(
            session.user, session.privilege, cookies.tag)

class Login:
    def GET(self):
        return web.seeother('/')

    def POST(self):
        (user, pw) = web.input().user, web.input().passwd
        try:
            ident = db.query('select * from users where user = $user',
                             vars = {'user': user})[0]
            if pw == ident['pass']:
                session.login = 1
                session.user = user
                session.privilege = ident['privilege']
                web.setcookie('tag', 'shit', 3600)
                web.seeother('/')
            else:
                session.login = 0
                session.privilege = 0
                return render.login_error()
        except:
            traceback.print_exc()
            session.login = 0
            session.privilege = 0
            return render.login_error()
class Logout:
    def GET(self):
        session.login = 0
        session.kill()
        return render.logout()

if __name__ == '__main__':
    app.run()
