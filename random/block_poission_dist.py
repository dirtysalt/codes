#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

# https://twitter.com/SatoshiLite/status/978913057999998976

import numpy as np


def run(lam, thres, n):
    values = np.random.poisson(lam=lam, size=n)
    values = np.array([x for x in values if x > thres])
    print('n = {}, # = {}, avg = {}'.format(n, len(values), values.mean()))


lam = 10
thres = 5
for n in (100 * 1000, 1000 * 1000, 5 * 1000 * 1000):
    run(lam, thres, n)
