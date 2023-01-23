#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from .worker import create_consumer, run_worker


def print_0(msg, st):
    print(msg)


def cc():
    return create_consumer(('test',), ['localhost:9092'], 'test-c0')


run_worker(cc, print_0, None, debug=True)
