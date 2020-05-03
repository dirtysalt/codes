#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from gevent.monkey import patch_all

patch_all()

import xutil
import os

from flask import Flask, request, session
from flask_socketio import Namespace, SocketIO

app = Flask(__name__)
logger = xutil.logger

sio = SocketIO(app, message_queue='redis://localhost/0', channel='flask-sio', async_mode='gevent')
namespace = '/fanout'
path = '{}.{}'.format(namespace, os.getpid())


@app.route('/', methods=['GET'])
def index():
    room = request.args.get('room', 0)
    logger.info('remote-peer: {}:{}, room: {}'.format(
        request.environ['REMOTE_ADDR'], request.environ['REMOTE_PORT'], room))
    return 'OK'


class MyNS(Namespace):
    def on_connect(self):
        logger.info('path = {}, on connect sid = {}, ({}:{}), headers = {}'.format(
            path, request.sid, request.environ['REMOTE_ADDR'], request.environ['REMOTE_PORT'],
            request.headers))

        sio.send('message: connect OK to all', namespace=namespace)
        sio.emit('my_event', 'my_event: connect OK', namespace=namespace)
        session['data'] = request.sid

    def on_disconnect(self):
        logger.info('path = {}, on disconnect. session data = {}'.format(path, session['data']))

    def on_message(self, message):
        logger.info('path = {}, on message. msg = {}'.format(path, message))

    def on_my_event(self, message):
        logger.info('path = {}, on my_event. msg = {}'.format(path, message))


sio.on_namespace(MyNS(namespace))

if __name__ == '__main__':
    import sys

    port = 8080
    if len(sys.argv) >= 2:
        port = int(sys.argv[1])
    host = '0.0.0.0'
    logger.info('running app on {}:{}'.format(host, port))
    # 如果使用socketio的话，那么use_reloader应该设置成为False
    # 否则会出现比较奇怪的问题
    sio.run(app, debug=True, host=host, port=port, use_reloader=False)
