#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt
import time

from Crypto.Cipher import AES
import gzip
import base64


def Decrypt(key: str, text: str) -> str:
    if len(key) < 32:
        key += ' ' * (32 - len(key))
    elif len(key) > 32:
        key = key[0:32]

    try:
        cipher = AES.new(bytes(key, encoding='utf-8'), AES.MODE_CBC, bytes(AES.block_size))
        ans = str(gzip.decompress(bytes.strip(cipher.decrypt(base64.b64decode(text)))), encoding='utf-8')
        return True
    except (OSError, EOFError):
        return False


def runTest(since):
    print('runTest since', since)
    cnt = 0
    last = time.time()
    for x in range(since, 10 ** 8):
        s = str(x)
        key = '0' * (8 - len(s)) + s
        cnt += 1
        if cnt % 100000 == 0:
            now = time.time()
            print('try', x, key, int(now - last))
            last = now
        if Decrypt(key,
                   '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'):
            print(key)
            break


import sys

since = int(sys.argv[1])
runTest(since)
