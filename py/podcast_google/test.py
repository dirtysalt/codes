#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

import os

data = open('resp.data', 'rb').read()
print('size = {}'.format(len(data)))

offset = 20
for x in range(offset):
    data2 = data[x:]
    with open('tmp.data', 'wb') as fh:
        fh.write(data2)
    code = os.system('cat tmp.data | protoc --decode_raw > resp.txt')
    if code == 0:
        print('use offset = {}'.format(x))
        print('head bytes = {}'.format(data[:x]))
        break
