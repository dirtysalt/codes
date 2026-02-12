#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class RangeSumer:
    def __init__(self, n):
        self.values = [0] * n

    def update(self, i, j, delta):
        for k in range(i, j + 1):
            self.values[k] += delta

    def query(self, i, j):
        acc = 0
        for k in range(i, j + 1):
            acc += self.values[k]
        return acc


class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        n = len(nums)
        prev = {}
        ans, acc = 0, 0
        MOD = 10 ** 9 + 7
        sumer = RangeSumer(n)
        for i in range(n):
            p = prev.get(nums[i], -1)
            prev[nums[i]] = i
            delta = 2 * sumer.query(p + 1, i - 1) + (i - 1 - p) + 1
            acc = (acc + delta) % MOD
            ans = (ans + acc) % MOD
            sumer.update(p + 1, i, 1)
        return ans % MOD


true, false, null = True, False, None
import aatest_helper

cases = [
    ([1, 2], 6,),
    ([1, 2, 1], 15),
    ([2, 2], 3),
    ([2, 2, 5], 12),
    ([2, 2, 5, 5], 22)
]

aatest_helper.run_test_cases(Solution().sumCounts, cases)

if __name__ == '__main__':
    pass
