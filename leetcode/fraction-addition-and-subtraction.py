#!/usr/bin/env python3
# coding:utf-8
# Copyright (C) dirlt

from typing import List
from collections import Counter, defaultdict, deque
from functools import lru_cache
import heapq

class Solution:
    def fractionAddition(self, expression: str) -> str:
        ops = []

        d = 0
        sign = 1
        for c in expression:
            if c in '+/-':
                ops.append(d*sign)
                d = 0
                sign = 1
                if c == '-':
                    sign = -1
                    c = '+'
                ops.append(c)
            else:
                d = d * 10 + ord(c) - ord('0')
        ops.append(d * sign)
        # print(ops)

        st = []
        i = 0
        while i < len(ops):
            if ops[i] == '/':
                st[-1] = (st[-1], ops[i+1])
                i += 2
            elif ops[i] == '+':
                i += 1
            else:
                st.append(ops[i])
                i += 1
        if st[0] == 0:
            st[0] = (0, 1)
        # print(st)

        def reduce(x, y):
            if x == 0: return (0, 1)
            sign = 1
            if x < 0:
                sign = -1 * sign
                x = -x
            if y < 0:
                sign = -1 * sign
                y = -y
            g = gcd(x, y)
            return (sign * x // g, y // g)

        def gcd(x, y):
            while y != 0:
                x, y = y, x % y
            return x

        (a, b) = (0, 1)
        for (c, d) in st:
            a, b = reduce(a * d + b * c, b * d)
        return '{}/{}'.format(a, b)

cases = [
    ('-1/2+1/2', '0/1'),
    ('-1/2+1/2+1/3','1/3'),
    ('1/3-1/2','-1/6'),
    ('5/3+1/3','2/1'),
]

import aatest_helper
aatest_helper.run_test_cases(Solution().fractionAddition, cases)


if __name__ == '__main__':
    pass
