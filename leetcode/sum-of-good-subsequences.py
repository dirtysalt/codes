#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def sumOfGoodSubsequences(self, nums: List[int]) -> int:
        # cache[x] x结尾的子序列和是多少，以及有多少个子序列
        cache = {}
        n = len(nums)

        MOD = 10 ** 9 + 7

        def update(x, a, b):
            oa, ob = cache.get(x, (0, 0))
            cache[x] = ((oa + a) % MOD, ob + b)

        for i in range(n):
            x = nums[i]
            dsum, dcnt = x, 1

            if (x - 1) in cache:
                a, b = cache[x - 1]
                dsum += a + b * x
                dcnt += b

            if (x + 1) in cache:
                a, b = cache[x + 1]
                dsum += a + b * x
                dcnt += b

            update(x, dsum, dcnt)
            # print(cache)

        ans = 0
        for k, (sum2, cnt) in cache.items():
            ans = (ans + sum2) % MOD
        return ans


true, false, null = True, False, None
import aatest_helper

cases = [
    ([1, 2, 1], 14),
    ([3, 4, 5], 40),
]

aatest_helper.run_test_cases(Solution().sumOfGoodSubsequences, cases)

if __name__ == '__main__':
    pass
