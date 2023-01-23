#!/usr/bin/env python3
# coding:utf-8
# Copyright (C) dirlt

from typing import List
from collections import Counter, defaultdict, deque
from functools import lru_cache
import heapq

class SolutionOld:
    def minAbsoluteSumDiff(self, nums1: List[int], nums2: List[int]) -> int:
        ans = 0

        tmp = sorted(nums1)

        n = len(nums1)
        for i in range(n):
            d = abs(nums1[i] - nums2[i])
            ans += d

        if ans == 0:
            return ans

        Max = 0
        for i in range(n):
            x = nums2[i]
            s, e = 0, n - 1
            while s <= e:
                m = (s + e) // 2
                if tmp[m] < x:
                    s = m + 1
                else:
                    e = m - 1
            # tmp[s] >= x
            res = 1 << 30
            if s < n:
                res = min(res, abs(tmp[s] - x))
            if (s - 1) >= 0:
                res = min(res, abs(tmp[s-1] - x))
            res = abs(nums1[i] - nums2[i]) - res
            Max = max(Max, res)

        ans -= Max
        MOD = 10 ** 9 + 7
        ans = ans % MOD
        return ans

class Solution:
    def minAbsoluteSumDiff(self, nums1: List[int], nums2: List[int]) -> int:
        ans = 0
        n = len(nums1)
        for i in range(n):
            d = abs(nums1[i] - nums2[i])
            ans += d

        tmp1 = []
        tmp2 = []
        for i in range(n):
            tmp1.append((nums1[i], i))
            tmp2.append((nums2[i], i))
        tmp1.sort()
        tmp2.sort()

        j = 0
        Max = 0
        for i in range(n):
            while j < n and tmp1[j][0] < tmp2[i][0]:
                j += 1

            res = 1 << 30
            s = j
            x = tmp2[i][0]
            if s < n:
                res = min(res, abs(tmp1[s][0] - x))
            if (s - 1) >= 0:
                res = min(res, abs(tmp1[s-1][0] - x))

            idx = tmp2[i][1]
            res = abs(nums1[idx] - nums2[idx]) - res
            Max = max(Max, res)

        ans -= Max
        MOD = 10 ** 9 + 7
        ans = ans % MOD
        return ans

cases = [
    ([1,7,5],  [2,3,5], 3),
    ([2,4,6,8,10], [2,4,6,8,10], 0),
    ([1,10,4,4,2,7], [9,3,5,1,7,4], 20),
]

import aatest_helper
aatest_helper.run_test_cases(Solution().minAbsoluteSumDiff, cases)


if __name__ == '__main__':
    pass
