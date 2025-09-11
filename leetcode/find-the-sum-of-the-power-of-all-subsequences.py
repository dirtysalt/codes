#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List
from collections import Counter, defaultdict, deque
from functools import lru_cache
import heapq


class Solution:
    def sumOfPower(self, nums: List[int], k: int) -> int:
        from collections import Counter
        now = Counter()
        MOD = 10 ** 9 + 7

        for i in range(len(nums)):
            z = nums[i]
            tmp = Counter()
            for x, c in now.items():
                tmp[x] = (2 * c) % MOD

            for x, c in now.items():
                value = x + z
                if value > k: continue
                tmp[value] += c

            tmp[z] += (2 ** i) % MOD

            now = tmp

        return now[k] % MOD


true, false, null = True, False, None
import aatest_helper

cases = [
    ([1, 2, 3], 3, 6),
    ([2, 3, 3], 5, 4),
    ([1, 2, 3], 7, 0),
]

aatest_helper.run_test_cases(Solution().sumOfPower, cases)

if __name__ == '__main__':
    pass
