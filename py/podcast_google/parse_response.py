#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

import brotli

from req_pb2 import SearchResponse

with open('response.content', 'rb') as fh:
    data = fh.read()


def ensure_string(s, encoding='utf8'):
    if isinstance(s, bytes):
        return s.decode(encoding)
    return s


def ensure_bytes(s, encoding='utf8'):
    if isinstance(s, str):
        return s.encode(encoding)
    return s


data = brotli.decompress(data)
# print(data)


resp = SearchResponse()
resp.ParseFromString(data[2:])
print(resp)
