#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

import asyncio
import logging
import time

from autobahn.asyncio.websocket import WebSocketClientFactory, WebSocketClientProtocol
from tdigest import TDigest

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


async def print_digest():
    global digest
    while True:
        with await digest.lock:
            logger.warning('DIGEST. count = {}, p50 = {}, p75 = {}, p90 = {}, p99 = {}'.format(
                digest.count(),
                digest.percentile(50),
                digest.percentile(75),
                digest.percentile(90),
                digest.percentile(99)))
        await asyncio.sleep(5)


global_index = 0


class MyClientProtocol(WebSocketClientProtocol):
    def onConnect(self, response):
        logger.info('onConnect. resp = {}'.format(response))
        global global_index
        self.index = global_index
        global_index += 1
        pass

    def onOpen(self):
        logger.info('on Open... ')
        pass

    # client连接上之后就只接收消息
    async def onMessage(self, payload, isBinary):
        logger.info('inst#{} recv {}'.format(self.index, payload))
        ts = int(payload)
        now = time.time()
        latency = now - ts
        with await digest.lock:
            digest.add(latency * 1000)


if __name__ == '__main__':
    factory = WebSocketClientFactory()
    factory.protocol = MyClientProtocol

    loop = asyncio.get_event_loop()
    inst_num = 5000
    insts = []
    for i in range(inst_num):
        coro = loop.create_connection(factory, '127.0.0.1', 8765)
        insts.append(coro)

    loop.run_until_complete(asyncio.gather(*insts))
    loop.run_until_complete(asyncio.gather(*[print_digest()]))
    loop.run_forever()
    loop.close()
