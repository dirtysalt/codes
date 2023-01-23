#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

import functools
import logging
import random
import time

import redis

logger = logging.getLogger()


# http://peter-hoffmann.com/2012/python-simple-queue-redis-queue.html


def _my_retry(wait_time=5):
    def fn(f):
        @functools.wraps(f)
        def wrapper(*args, **kwargs):
            while True:
                try:
                    return f(*args, **kwargs)
                except redis.connection.ConnectionError:
                    logger.debug('redis conn error. reconnect it after %.2f seconds' % wait_time)
                    time.sleep(wait_time)

        return wrapper

    return fn


class RedisQueue(object):
    """Simple Queue with Redis Backend"""

    def __init__(self, name, namespace='queue', **redis_kwargs):
        """The default connection parameters are: host='localhost', port=6379, db=0"""
        self.__db = redis.Redis(**redis_kwargs)
        self.key = '%s:%s' % (namespace, name)
        self.name = name

    @_my_retry()
    def clear(self):
        return self.__db.delete(self.key)

    @_my_retry()
    def qsize(self):
        """Return the approximate size of the queue."""
        return self.__db.llen(self.key)

    def empty(self):
        """Return True if the queue is empty, False otherwise."""
        return self.qsize() == 0

    @_my_retry()
    def put(self, item):
        """Put item into the queue."""
        self.__db.rpush(self.key, item)

    @_my_retry()
    def get(self, block=True, timeout=None):
        """Remove and return an item from the queue.

        If optional args block is true and timeout is None (the default), block
        if necessary until an item is available."""
        if block:
            item = self.__db.blpop(self.key, timeout=timeout)
            if item:
                item = item[1]
        else:
            item = self.__db.lpop(self.key)
        return item

    def get_nowait(self):
        """Equivalent to get(False)."""
        return self.get(False)

    def sync(self, size, min_sleep=5, max_sleep=10):
        while True:
            mysize = self.qsize()
            if mysize >= size:
                interval = random.randint(min_sleep * 1000, max_sleep * 1000) * 0.001
                logger.debug('current qsize = %d(> %d). sleep %.2f seconds' % (mysize, size, interval))
                time.sleep(interval)
            else:
                break
