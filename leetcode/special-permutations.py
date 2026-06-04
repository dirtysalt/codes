#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List
from collections import Counter, defaultdict, deque
from functools import lru_cache
import heapq


class Solution:
    def specialPerm(self, nums: List[int]) -> int:
        from functools import cache
        n = len(nums)

        @cache
        def search(p, mask):
            if mask == 0: return 1
            res = 0
            for i in range(n):
                x = nums[i]
                if mask & (1 << i) and (p == -1 or x % p == 0 or p % x == 0):
                    mask2 = mask & ~(1 << i)
                    res += search(x, mask2)
            return res

        MOD = 10 ** 9 + 7
        ans = search(-1, (1 << n) - 1)
        return ans % MOD


true, false, null = True, False, None
import aatest_helper

cases = [
    ([2, 3, 6], 2),
    ([1, 4, 3], 2),
]

aatest_helper.run_test_cases(Solution().specialPerm, cases)

if __name__ == '__main__':
    pass
