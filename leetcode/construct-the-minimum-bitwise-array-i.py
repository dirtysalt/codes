#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from functools import cache
from typing import List


class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        inf = 1 << 31

        @cache
        def dfs(x, bit, c):
            if bit == 32:
                return 0

            if x & (1 << bit):
                if c == 1:
                    r0 = dfs(x, bit + 1, 1) | (1 << bit)
                    r1 = dfs(x, bit + 1, 0)
                    return min(r0, r1)
                else:
                    r = dfs(x, bit + 1, 0) | (1 << bit)
                    return r
            else:
                if c == 1:
                    return inf
                else:
                    r = dfs(x, bit + 1, 0)
                    return r

        ans = []
        for x in nums:
            r = dfs(x, 0, 1)
            if r >= inf:
                r = -1
            ans.append(r)
        return ans


true, false, null = True, False, None
import aatest_helper

cases = [
    ([2, 3, 5, 7], [-1, 1, 4, 3]),
    ([11, 13, 31], [9, 12, 15]),
    ([3391, 499, 811, 5851, 3943, 421, 4051, 1187, 1601, 9781, 3617],
     [3359, 497, 809, 5849, 3939, 420, 4049, 1185, 1600, 9780, 3616]),
]

aatest_helper.run_test_cases(Solution().minBitwiseArray, cases)

if __name__ == '__main__':
    pass
