#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def minOperations(self, target: List[int], arr: List[int]) -> int:
        index = {}
        for i in range(len(target)):
            index[target[i]] = i

        tmp = [-1] * len(arr)
        for i in range(len(arr)):
            x = arr[i]
            if x in index:
                tmp[i] = index[x]

        # find LIS of tmp
        dp = []
        for x in tmp:
            if x == -1: continue
            s, e = 0, len(dp) - 1
            while s <= e:
                m = (s + e) // 2
                if dp[m] >= x:
                    e = m - 1
                else:
                    s = m + 1
            # put at s
            if s == len(dp):
                dp.append(x)
            else:
                dp[s] = x

        # print(tmp, dp)
        ans = len(target) - len(dp)
        return ans


cases = [
    ([5, 1, 3], [9, 4, 2, 3, 4], 2),
    ([6, 4, 8, 1, 3, 2], [4, 7, 6, 2, 3, 8, 6, 1], 3)
]

import aatest_helper

aatest_helper.run_test_cases(Solution().minOperations, cases)
