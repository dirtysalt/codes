#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

import base64

from req_pb2 import SearchRequest


def ensure_string(s, encoding='utf8'):
    if isinstance(s, bytes):
        return s.decode(encoding)
    return s


def ensure_bytes(s, encoding='utf8'):
    if isinstance(s, str):
        return s.encode(encoding)
    return s


def make_request():
    req = SearchRequest()
    # header = req.header
    # header.a.b.a = 6
    # header.a.b.b = "2"
    # header.b.c.a = bytes.fromhex("53552d6e")

    payload = req.payload
    payload.query = "joe rogan"
    # payload.a = 36
    # payload.b = 3

    return req


req = make_request()
req_bytes = req.SerializeToString()
req_b64 = ensure_string(base64.b64encode(req_bytes))
print(req_b64)

import requests

url = 'https://www.google.com'
path = '/httpservice/web/WernickeService/GetSearchResults'
headers = {
    "User-Agent": "Mozilla/5.0 (Linux; Android 5.0.2; SM-A700YD Build/LRX22G; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/43.0.2357.121 Mobile Safari/537.36 GSA/8.59.7.21.arm",
    "Accept-Encoding": "gzip, deflate, br",
    "X-Protobuffer-Request-Payload": req_b64
}
r = requests.get(url + path, headers=headers)
content = r.content

with open('response.content', 'wb') as fh:
    fh.write(content)
