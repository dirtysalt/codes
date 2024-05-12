#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt
from typing import List


class Solution:
    def findPermutation(self, nums: List[int]) -> List[int]:
        n = len(nums)

        import functools
        @functools.cache
        def dfs(last, mask):
            if mask == ((1 << n) - 1):
                return abs(last - nums[0]), [last]

            from math import inf
            ans = inf
            perm = None
            for j in range(n):
                if mask & (1 << j) == 0:
                    c = abs(last - nums[j])
                    r, p = dfs(j, mask | (1 << j))
                    c += r
                    if c > ans: continue
                    if c < ans or (perm is None or perm > p):
                        perm = p
                    ans = c
            return ans, [last] + perm

        ans, perm = dfs(0, 1)
        print(ans)
        return perm


true, false, null = True, False, None
import aatest_helper

cases = [
    ([1, 0, 2], [0, 1, 2]),
    ([0, 2, 1], [0, 2, 1]),
    ([1, 3, 2, 0], [0, 3, 1, 2]),
    ([0, 2, 1, 3, 4], [0, 2, 3, 4, 1]),
    (list(range(14)), list(range(14))),
]

aatest_helper.run_test_cases(Solution().findPermutation, cases)

if __name__ == '__main__':
    pass
