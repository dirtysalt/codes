#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

# http://cn.python-requests.org/zh_CN/latest/api.html

import requests

ss = requests.session()
r = ss.post('http://localhost:10001/', files={'xfile': ('test.py', open('test.py'))})
print(r.status_code)
