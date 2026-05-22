#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

step = 0

def f(n, x, y, z):
    global step
    if n == 1:
        print('move 1: %d -> %d' % (x, z))
        step += 1
        return
    f(n - 1, x, z, y)
    # move N x->z
    print('move %d: %d -> %d' % (n, x, z))
    step += 1
    f(n - 1, y, x, z)


f(4, 1, 2, 3)
print(step)

if __name__ == '__main__':
    pass
