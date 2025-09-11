#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class BitIndexTree:
    def __init__(self, n):
        self.arr = [0] * (n + 1)
        self.n = n

    def add(self, i, x):
        i = i + 1
        n = self.n
        while i <= n:
            self.arr[i] += x
            i = i + (i & -i)

    def get(self, i):
        i = i + 1
        ans = 0
        while i > 0:
            ans += self.arr[i]
            i = i - (i & -i)
        return ans


class Solution:
    def createSortedArray(self, instructions: List[int]) -> int:
        ss = list(set(instructions))
        ss.sort()
        n = len(ss)
        index = {}
        for i in range(n):
            x = ss[i]
            index[x] = i

        from collections import Counter
        cnt = Counter()
        tree = BitIndexTree(n)
        ans = 0
        for i in range(len(instructions)):
            x = instructions[i]
            cnt[x] += 1
            idx = index[x]
            tree.add(idx, 1)
            v = tree.get(idx)
            a = v - cnt[x]
            b = (i + 1) - v
            # print(x, v, cnt[x], a, b, min(a, b))
            ans += min(a, b)

        MOD = 10 ** 9 + 7
        ans = ans % MOD
        return ans


cases = [
    ([1, 5, 6, 2], 1),
    ([1, 2, 3, 6, 5, 4], 3),
    ([1, 3, 3, 3, 2, 4, 2, 1, 2], 4)
]

import aatest_helper

aatest_helper.run_test_cases(Solution().createSortedArray, cases)
