#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt
from typing import List


class Solution:
    def countSubMultisets(self, nums: List[int], L: int, R: int) -> int:
        from collections import Counter
        cnt = Counter(nums)

        f = [cnt[0] + 1] + [0] * R
        del cnt[0]

        upper = 0
        MOD = 10 ** 9 + 7
        for x, c in cnt.items():
            new_f = f.copy()
            upper = min(upper + x * c, R)
            for j in range(x, upper + 1):
                new_f[j] += new_f[j - x]
                if j >= (c + 1) * x:
                    new_f[j] -= f[j - (c + 1) * x]
                new_f[j] %= MOD
            f = new_f
        return sum(f[L:]) % MOD


class Solution:
    def countSubMultisets(self, nums: List[int], L: int, R: int) -> int:
        from collections import Counter
        cnt = Counter(nums)

        f = [cnt[0] + 1] + [0] * R
        del cnt[0]

        upper = 0
        MOD = 10 ** 9 + 7
        for x, c in cnt.items():
            upper = min(upper + x * c, R)
            for j in range(x, upper + 1):
                f[j] = (f[j] + f[j - x]) % MOD
            for j in reversed(range((c + 1) * x, upper + 1)):
                f[j] = (f[j] - f[j - (c + 1) * x]) % MOD

        return sum(f[L:]) % MOD


true, false, null = True, False, None
import aatest_helper

cases = [
    aatest_helper.OrderedDict(nums=[1, 2, 2, 3], l=6, r=6, res=1),
    aatest_helper.OrderedDict(nums=[2, 1, 4, 2, 7], l=1, r=5, res=7),
    aatest_helper.OrderedDict(nums=[1, 2, 1, 3, 5, 2], l=3, r=5, res=9),
    aatest_helper.OrderedDict(nums=[0, 0, 0, 0, 0], l=0, r=0, res=6),
]

aatest_helper.run_test_cases(Solution().countSubMultisets, cases)

if __name__ == '__main__':
    pass
