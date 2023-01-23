#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt


def ip2tocdr(start, end):
    def ip2value(ip):
        val = 0
        for s in ip.split('.'):
            x = int(s)
            val = val * 256 + x
        return val

    def value2ip(val):
        res = []
        for i in range(4):
            x = val % 256
            val = val // 256
            res.append(str(x))
        res = res[::-1]
        return '.'.join(res)

    def zeros(x):
        cnt = 0
        while x & 0x1 == 0:
            cnt += 1
            x >>= 1
        return cnt

    start_value = ip2value(start)
    end_value = ip2value(end)

    # core algorithm.
    x = start_value
    res = []
    while x <= end_value:
        zs = zeros(x)
        while (x + (1 << zs) - 1) > end_value:
            zs -= 1
        res.append((x, 32 - zs))
        x += (1 << zs)

    return [value2ip(x[0]) + '/' + str(x[1]) for x in res]


cases = [
    ('5.10.64.0', '5.10.127.255', ['5.10.64.0/18'])
]

for (start, end, exp) in cases:
    res = ip2tocdr(start, end)
    print(res, exp)
