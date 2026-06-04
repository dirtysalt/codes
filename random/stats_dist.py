#!/usr/bin/env python
#coding:utf-8
#Copyright (C) dirlt

import matplotlib.pyplot as plt
import random
import math

def cdf(ps):
    ps.sort()
    sz = len(ps)
    vs = [i * 1.0 / sz for i in range(0, sz)]
    return vs

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

def plot_points(func, N = 10000):
    ps = [func() for i in range(0, N)]
    vs = cdf(ps)
    plt.subplot(2,1,1)
    plt.plot(ps, vs)
    plt.subplot(2,1,2)
    plt.plot(pdf(ps))
    plt.show()

def plot_expovariate():
    plot_points(lambda : random.expovariate(2.0))
def plot_lognormvariate():
    plot_points(lambda : random.lognormvariate(2.0, 1.0))
def plot_gauss():
    plot_points(lambda : random.gauss(2.0, 1.0))
def plot_pareto():
    plot_points(lambda : random.paretovariate(5.0))

# plot_lognormvariate()
# plot_expovariate()
# plot_gauss()
plot_pareto()
