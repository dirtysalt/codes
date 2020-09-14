#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt


import asyncio
import logging
import time

from autobahn.asyncio.websocket import WebSocketClientFactory, WebSocketClientProtocol
from tdigest import TDigest

global_index = 0
logger = logging.getLogger()
DEFAULT_LOGGING_FORMAT = '[%(asctime)s][%(levelname)s]%(filename)s@%(lineno)d: %(msg)s'
logging.basicConfig(level=logging.WARN, format=DEFAULT_LOGGING_FORMAT)


class Digest:
    def __init__(self):
        self.digest = TDigest()
        self.digest.update(0)
        self._count = 0
        self.lock = asyncio.Lock()

    def add(self, v):
        self.digest.update(v)
        self._count += 1

    def percentile(self, v):
        return self.digest.percentile(v)

    def count(self):
        return self._count


digest = Digest()


# 打印ping-pong的延迟情况
async def print_digest():
    global digest
    while True:
        with await digest.lock:
            logger.warning('DIGEST. count = {},  p50 = {}, p75 = {}, p90 = {}, p99 = {}'.format(
                digest.count(), digest.percentile(50),
                digest.percentile(75),
                digest.percentile(90),
                digest.percentile(99)))
        await asyncio.sleep(5)


class MyClientProtocol(WebSocketClientProtocol):
    async def onConnect(self, response):
        logger.info('on Connect ...')
        global global_index
        self.index = global_index
        global_index += 1

    async def onOpen(self):
        logger.info('on Open... ')
        self.sendMessage(b'ping')
        self.ping = time.time()
        pass

    async def onMessage(self, payload, isBinary):
        if payload != b'pong':
            return
        now = time.time()
        latency = now - self.ping
        global digest
        with await digest.lock:
            digest.add(latency * 1000)
        logger.info('inst#{} recv {}. latency = {}'.format(self.index, payload, latency))
        self.sendMessage(b'ping')
        self.ping = time.time()


if __name__ == '__main__':
    factory = WebSocketClientFactory()
    factory.protocol = MyClientProtocol

    loop = asyncio.get_event_loop()
    inst_num = 10
    insts = []
    for i in range(inst_num):
        coro = loop.create_connection(factory, '127.0.0.1', 8765)
        insts.append(coro)

    loop.run_until_complete(asyncio.gather(*insts))
    loop.run_until_complete(asyncio.gather(*[print_digest()]))
    loop.run_forever()
    loop.close()
