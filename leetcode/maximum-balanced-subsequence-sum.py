#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def maxBalancedSubsequenceSum(self, nums: List[int]) -> int:
        # dp[i] = max(dp[j]) + nums[i] if (i - j) <= nums[i] - nums[j]
        # i - nums[i] <= j - nums[j]

        diff = [i - nums[i] for i in range(len(nums))]
        diff.sort(reverse=True)
        pos = {}
        for d in diff:
            if d not in pos:
                pos[d] = len(pos)
        N = len(pos)

        INF = 1 << 63
        SZ = 1
        while SZ < N:
            SZ = SZ * 2
        MAX = [-INF] * (2 * SZ)

        def update_max(p, v):
            k = p + SZ
            MAX[k] = max(MAX[k], v)
            while k != 1:
                p = k // 2
                MAX[p] = max(MAX[2 * p], MAX[2 * p + 1])
                k = p

        def query_max(p):
            def do(i, j, k, s, sz):
                if i <= s <= (s + sz - 1) <= j:
                    return MAX[k]
                mid = s + sz // 2
                res = -INF
                if i < mid:
                    a = do(i, j, 2 * k, s, sz // 2)
                    res = max(res, a)
                if j >= mid:
                    a = do(i, j, 2 * k + 1, mid, sz // 2)
                    res = max(res, a)
                return res

            return do(0, p, 1, 0, SZ)

        ans = -INF
        for i in range(len(nums)):
            d = i - nums[i]
            p = pos[d]
            value = nums[i]
            last = query_max(p)
            value += max(last, 0)
            update_max(p, value)
            ans = max(ans, value)

        return ans


true, false, null = True, False, None
import aatest_helper

cases = [
    ([3, 3, 5, 6], 14),
    ([5, -1, -3, 8], 13),
    ([-2, -1], -1,),
    ([3, -1, -9, 5, -7, 9, 6], 14),
    ([-3, 7, 0, 4, 6], 10,),
    ([-43, 29, -17, 25, 26, -36, 14, -5, 43, -43, -50, 31, 38, -47, -47, 24, -9, -27, 42], 94),
]

aatest_helper.run_test_cases(Solution().maxBalancedSubsequenceSum, cases)

if __name__ == '__main__':
    pass
