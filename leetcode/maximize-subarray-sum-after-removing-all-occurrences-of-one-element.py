#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def maxSubarraySum(self, nums: List[int]) -> int:
        inf = (1 << 63) - 1

        def test(nums):
            n = len(nums)
            res = -inf
            dp = [-inf] * n
            last = {}
            pre = [0]
            for i in range(n):
                x = nums[i]
                pre.append(pre[-1] + x)
                if x in last:
                    j = last[x]
                    dp[i] = dp[j] + pre[-1] - pre[j] - 2 * x
                dp[i] = max(dp[i], res)
                res = max(res, 0) + x
                last[x] = i
            return dp, res

        left, ans = test(nums)
        right, ans = test(nums[::-1])
        right = right[::-1]

        for i in range(len(nums)):
            ans = max(ans, left[i] + right[i], left[i], right[i])
        return ans


true, false, null = True, False, None
import aatest_helper

cases = [
    ([-3, 2, -2, -1, 3, -2, 3], 7),
    ([1, 2, 3, 4], 10),
]

aatest_helper.run_test_cases(Solution().maxSubarraySum, cases)

if __name__ == '__main__':
    pass
