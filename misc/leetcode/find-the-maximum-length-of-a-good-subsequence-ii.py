#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class State:
    def __init__(self):
        self.values = {}
        self.sizes = []

    def check(self, v):
        if v not in self.values:
            self.values[v] = 0
            self.sizes.append((0, v))

    def update(self, v, sz):
        self.check(v)
        prev = self.values[v]
        if sz > prev:
            self.values[v] = sz
            self.sizes.append((sz, v))
            self.fix_sizes()

    def fix_sizes(self):
        self.sizes.sort(reverse=True)
        tmp = []
        for sz2, v2 in self.sizes:
            if any(x[1] == v2 for x in tmp): continue
            tmp.append((sz2, v2))
            if len(tmp) == 2: break
        self.sizes = tmp

    def query(self, v):
        self.check(v)
        sz = self.values[v]
        next_sz = 0
        for sz2, v2 in self.sizes:
            if v == v2: continue
            next_sz = sz2
            break
        return sz, next_sz

    def max_size(self):
        return self.sizes[0][0]

    def __repr__(self):
        return f"values = {self.values}, sizes = {self.sizes}"


class Solution:
    def maximumLength(self, nums: List[int], k: int) -> int:
        states = [State() for _ in range(k + 1)]
        for x in nums:
            for j in reversed(range(k + 1)):
                sz, next_sz = states[j].query(x)
                states[j].update(x, sz + 1)
                if j < k:
                    states[j + 1].update(x, next_sz + 1)

        ans = 0
        for j in range(0, k + 1):
            ans = max(ans, states[j].max_size())
        return ans


true, false, null = True, False, None
import aatest_helper

cases = [
    aatest_helper.OrderedDict(nums=[1, 2, 1, 1, 3], k=2, res=4),
    aatest_helper.OrderedDict(nums=[1, 2, 3, 4, 5, 1], k=0, res=2),
    ([2, 5], 1, 2),
    ([29, 29, 28], 0, 2)
]

aatest_helper.run_test_cases(Solution().maximumLength, cases)

if __name__ == '__main__':
    pass
