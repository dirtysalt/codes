#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from redis_queue import RedisQueue

command_queue = RedisQueue('command')
command_queue.put('trigger')
