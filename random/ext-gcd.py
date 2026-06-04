#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

def ext_gcd(a, b):
    # ax - by = m
    # b(a//b*x-y) - (a%b)(-x) = m
    # bx' - (a%b)y' = m
    if b == 0:
        return a, 1, 0
    m, x2, y2 = ext_gcd(b, a % b)
    x = -y2
    y = a // b * (-y2) - x2
    return m, x, y


for a, b in ((10, 6), (5, 3), (20, 11), (20, 15)):
    m, x, y = ext_gcd(a, b)
    if x < 0 and y < 0:
        a, b = b, a
        x, y = -y, -x
    print('{}*{}-{}*{}={}'.format(a, x, b, y, m))

if __name__ == '__main__':
    pass
