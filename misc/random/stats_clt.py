#!/usr/bin/env python
#coding:utf-8
#Copyright (C) dirlt

# https://en.wikipedia.org/wiki/Central_limit_theorem

import matplotlib.pyplot as plt
import random
import numpy as np

def pdf(ps):
    bucket_n = 1000
    mx = max(ps)
    mn = min(ps)
    interval = (mx - mn) / bucket_n
    vs = [0] * bucket_n
    for p in ps:
        off = int((p - mn) / interval)
        if off >= bucket_n: off = bucket_n - 1
        vs[off] += 1
    vs = [x * 1.0 / len(ps) for x in vs]
    return vs

streams = [{'func': random.expovariate,
            'args': [(1.0,), (2.0,), (3.0,), (4.0,)]},
           {'func': random.gauss,
            'args': [(2.0, 1.0), (1.0, 2.0), (3.0, 4.0), (2.0, 4.0)]},
           {'func': random.paretovariate,
            'args': [(5.0,), (6.0,), (7.0,), (8.0,)]}]
def gen():
    values = []
    for s in streams:
        f = s['func']
        args = s['args']
        values.extend([f(*x) for x in args])
    return sum(values) * 1.0 / len(values)

N = 10000
ps = np.array([gen() for i in range(0, N)])
vs = np.array(pdf(ps))
xs = np.arange(ps.min(), ps.max(), (ps.max() - ps.min()) * 1.0 / vs.size)
print('mean = {}, std ={}'.format(ps.mean(), ps.std()))
plt.plot(xs, vs)
plt.show()
