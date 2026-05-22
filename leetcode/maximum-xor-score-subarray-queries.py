#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution2:
    def maximumSubarrayXor(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        def handle(l, r):
            t = nums[l:r + 1]
            res = max(t)
            while len(t) != 1:
                t2 = []
                for i in range(1, len(t)):
                    t2.append(t[i - 1] ^ t[i])
                res = max(res, max(t2))
                t = t2
            return res

        ans = []
        for l, r in queries:
            ret = handle(l, r)
            ans.append(ret)
        return ans


class Solution:
    def maximumSubarrayXor(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        n = len(nums)

        pre = []
        t = nums
        pre.append(t)
        while len(t) != 1:
            t2 = []
            for i in range(1, len(t)):
                t2.append(t[i - 1] ^ t[i])
            pre.append(t2)
            t = t2

        left = [[0] * (n - i + 1) for i in range(n)]
        for i in range(n):
            sz = 1
            while i >= 0:
                left[i][sz] = pre[sz - 1][i]
                sz += 1
                i -= 1

        for i in range(n):
            for sz in range(1, len(left[i])):
                left[i][sz] = max(left[i][sz], left[i][sz - 1])

        # L[i][sz] = max(L[i][sz], .L[i+1][sz-1], L[i+2][sz-2]...)
        # L[i+1][sz-1] = max(L[i+1][sz-1], L[i+2][sz-2]...)
        for sz in range(1, n + 1):
            for i in range(n - sz + 1):
                if (i + 1) < n:
                    left[i][sz] = max(left[i][sz], left[i + 1][sz - 1])

        ans = []
        # 10 ** 5
        for q in queries:
            l, r = q
            ans.append(left[l][r - l + 1])
        return ans


true, false, null = True, False, None
import aatest_helper

cases = [
    aatest_helper.OrderedDict(nums=[2, 8, 4, 32, 16, 1], queries=[[0, 2], [1, 4], [0, 5]], res=[12, 60, 60]),
    aatest_helper.OrderedDict(nums=[0, 7, 3, 2, 8, 5, 1], queries=[[0, 3], [1, 5], [2, 4], [2, 6], [5, 6]],
                              res=[7, 14, 11, 14, 5])
]

aatest_helper.run_test_cases(Solution().maximumSubarrayXor, cases)

if __name__ == '__main__':
    pass
