#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

import socketio

import xutil

logger = xutil.logger
namespace = '/fanout'


class MyNS(socketio.ClientNamespace):
    def on_connect(self):
        logger.info('on connect')
        self.emit('message', 'message from client')
        self.emit('my_event', 'my_event from client')

    def on_disconnect(self):
        logger.info('on disconnect')

    def on_message(self, data):
        logger.info('on message. msg = {}'.format(data))

    def on_my_event(self, data):
        logger.info('on my_event. msg = {}'.format(data))


sio = socketio.Client()
ns = MyNS(namespace)
sio.register_namespace(ns)
sio.connect('http://127.0.0.1:8080')

ns.emit('my_event', '!!! my event from client')
ns.emit('message', '!!! message from client')

sio.wait()
