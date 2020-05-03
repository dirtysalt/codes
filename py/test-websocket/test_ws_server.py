#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

import asyncio
import logging
import time

from autobahn.asyncio.websocket import WebSocketServerFactory, WebSocketServerProtocol
from redis_queue import RedisQueue

# # 这个地方似乎有bug, 如果使用uvloop的话，整个代码会hang住
# import uvloop
#
# asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())

logger = logging.getLogger()
DEFAULT_LOGGING_FORMAT = '[%(asctime)s][%(levelname)s]%(filename)s@%(lineno)d: %(msg)s'
logging.basicConfig(level=logging.WARN, format=DEFAULT_LOGGING_FORMAT)


class ConnectionManeger:
    def __init__(self):
        self.conns = dict()

    def add(self, peer, conn):
        self.conns[peer] = conn

    def remove(self, peer):
        if peer in self.conns:
            del self.conns[peer]

    def getall(self):
        yield from self.conns.values()

    def count(self):
        return len(self.conns)


connection_manager = ConnectionManeger()
connection_channel = asyncio.Queue()


async def listen_command():
    global connection_manager, connection_channel
    while True:
        msg = await connection_channel.get()
        logger.info('got message from channel. value = {}'.format(msg))
        payload = msg
        for conn in connection_manager.getall():
            conn.sendMessage(payload)


command_queue = RedisQueue('command')


# 决定是否从redis queue里面收取消息然后广播到所有连接上.
async def read_command():
    evloop = asyncio.get_event_loop()
    while True:
        item = await evloop.run_in_executor(None, command_queue.get, (30,))
        if item is None:
            continue
        ts = int(time.time())
        msg = str(ts).encode('utf8')
        logger.info('get from queue {}, send msg {}'.format(item, msg))
        await connection_channel.put(msg)


async def write_command():
    evloop = asyncio.get_event_loop()
    idx = 0
    while True:
        msg = 'command #%d' % idx
        await evloop.run_in_executor(None, command_queue.put, (msg,))
        logger.info('put queue. value = {}'.format(msg))
        idx += 1
        await asyncio.sleep(5)


async def print_stats():
    while True:
        logger.warning('total connections = {}'.format(connection_manager.count()))
        # ts = int(time.time())
        # msg = str(ts).encode('utf8')
        # logger.info('put msg = {}'.format(msg))
        # await connection_channel.put(msg)
        await asyncio.sleep(5)


class MyServerProtocol(WebSocketServerProtocol):
    async def onMessage(self, payload, isBinary):
        logger.info('onMessage. {}, {}'.format(payload, isBinary))
        self.sendMessage(b'pong')
        # self.sendMessage(payload, isBinary)

    async def onConnect(self, request):
        logger.info('onConnect {}'.format(request))
        self.peer = request.peer
        connection_manager.add(self.peer, self)
        pass

    async def onClose(self, wasClean, code, reason):
        logger.info('onClose {}, {}, {}'.format(wasClean, code, reason))
        connection_manager.remove(self.peer)
        pass

    async def onOpen(self):
        logger.info('onOpen ...')
        pass


def main():
    factory = WebSocketServerFactory()
    factory.protocol = MyServerProtocol
    loop = asyncio.get_event_loop()
    coro = loop.create_server(factory, '127.0.0.1', 8765)
    server = loop.run_until_complete(coro)
    loop.run_until_complete(asyncio.gather(*[listen_command(),
                                             read_command(),
                                             # write_command(),
                                             print_stats()]))
    loop.run_forever()
    loop.close()
    server.close()


if __name__ == '__main__':
    main()
