#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from gevent import monkey

monkey.patch_all()

import xutil

from flask import Flask, request
from flask_socketio import Namespace, SocketIO

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app, message_queue='redis://localhost/0', channel='socketio-test')
logger = xutil.logger

total_connection = 0
ns_name = '/fanout'


@app.route(ns_name, methods=['GET'])
def handle_fanout():
    message = 'addr = {}, port = {}, room = {}, conn = {}'.format(request.environ['REMOTE_ADDR'],
                                                                  request.environ['REMOTE_PORT'],
                                                                  request.args.get('room', 0),
                                                                  total_connection)
    return message


class FanoutNamespace(Namespace):
    def on_connect(self):
        msg = 'on connect sid = {}, ({}:{})'.format(
            request.sid, request.environ['REMOTE_ADDR'],
            request.environ['REMOTE_PORT'])
        logger.info(msg)
        global total_connection
        total_connection += 1
        # self.send('ACK', room=request.sid)
        pass

    def on_disconnect(self):
        logger.info('disconnect sid = {}'.format(request.sid))
        global total_connection
        total_connection -= 1
        pass

    def on_message(self, message):
        pass

    def on_my_event(self, message):
        pass


socketio.on_namespace(FanoutNamespace(ns_name))

if __name__ == '__main__':
    import sys

    port = 8080
    if len(sys.argv) >= 2:
        port = int(sys.argv[1])
    socketio.run(app, debug=False, port=port, host='0.0.0.0')
