#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

import socketio
from aiohttp import web

import xutil

logger = xutil.logger
channel = socketio.AsyncRedisManager('redis://localhost:6379/0', channel='socketio-test')

server_args = {
    'allow_upgrades': True,
}
sio = socketio.AsyncServer(client_manager=channel, **server_args)

app = web.Application()
sio.attach(app)


async def handle_fanout(request):
    return web.Response(text='query = "{}"'.format(request.query_string))


namespace = '/'


@sio.on('connect', namespace=namespace)
async def connect(sid, _environ):
    logger.info('connect. sid = {}'.format(sid))


@sio.on('disconnect', namespace=namespace)
async def disconnect(sid):
    logger.info('disconnect. sid = {}'.format(sid))


app.router.add_get(namespace, handle_fanout)

if __name__ == '__main__':
    import sys

    port = 8080
    if len(sys.argv) >= 2:
        port = int(sys.argv[1])

    web.run_app(app, host='0.0.0.0', port=port)
