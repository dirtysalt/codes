#!/usr/bin/env python
#coding:utf-8
#Copyright (C) dirlt

# https://en.wikipedia.org/wiki/Monty_Hall_problem
import random
def run_once(n):
    def r(): return random.randint(0, n-1)
    # car is at #x.
    x = r()
    # choice is at #c.
    c = r()
    # first choice is, to stick to original plan.
    v1 = (x == c)
    # second choice is, to change to another one.
    # open one except #x and #c.
    while True:
        t = r()
        if not (t == x or t == c): break
    # now #t is open, choose one except #t and #c.
    while True:
        c2 = r()
        if not (c2 == t or c2 == c): break
    v2 = (x == c2)
    return (v1, v2)

random.seed(100)
N = 100000
DOORS = 3
(v1, v2) = (0, 0)
for x in range(0, N):
    (u1, u2) =  run_once(DOORS)
    v1 += u1
    v2 += u2
print('prob p1 = %.2f, p2 = %.2f' % (v1 * 100.0 / N, v2 * 100.0 / N))
