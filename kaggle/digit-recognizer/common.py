#!/usr/bin/env python
#coding:utf-8
#Copyright (C) dirlt

# http://www.kaggle.com/c/digit-recognizer

import numpy as np
import time

def read_in(s, test = False):
    s = s.strip()
    ss = map(lambda x: int(x), s.split(','))
    if not test: return (ss[1:], ss[0])
    else: return ss

def read_train(n):
    f = open('train.csv')
    xs = []
    ys = []
    for s in f:
        if s.startswith('label'): continue
        if not n: break
        n -= 1
        (x, y) = read_in(s)
        xs.append(np.array(x))
        ys.append(y)
    return (np.array(xs).astype(np.float32) * 1.0 / 256, np.array(ys).astype(np.float32))

def read_test(n):
    f = open('test.csv')
    xs = []
    for s in f:
        if s.startswith('pixel'): continue
        if not n: break
        n -= 1
        x = read_in(s, True)
        xs.append(np.array(x))
    return np.array(xs).astype(np.float32) * 1.0 / 256

def write_result(ys, fname):
    f = open(fname, 'w')
    f.write('ImageId,Label\n')
    for i in xrange(0, len(ys)):
        y = ys[i]
        f.write('%d,%d\n' % (i+1, y))
    f.close()

def find_max_idx(xs):
    n = xs.shape[0]
    mx = xs.max()
    for i in range(0, n):
        if xs[i] == mx: return i
    assert(0)

_ts = 0
def start_timer():
    global _ts
    _ts = time.time()
def print_timer(msg):
    global _ts
    _now = time.time()
    print('%s: %.2f seconds' % (msg, _now - _ts))
    _ts = _now
