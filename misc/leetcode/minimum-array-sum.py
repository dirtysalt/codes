#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def minArraySum(self, nums: List[int], k: int, op1: int, op2: int) -> int:
        n = len(nums)

        import functools
        @functools.cache
        def dfs(i, a, b):
            if i == len(nums):
                return 0

            res = []
            # no op
            x = dfs(i + 1, a, b) + nums[i]
            res.append(x)

            # op1
            if a > 0:
                x = dfs(i + 1, a - 1, b) + (nums[i] + 1) // 2
                res.append(x)

            # op2
            if b > 0 and nums[i] >= k:
                x = dfs(i + 1, a, b - 1) + (nums[i] - k) if nums[i] >= k else nums[i]
                res.append(x)

            # op1 -> op2
            if a > 0 and b > 0 and nums[i] >= k:
                x = nums[i]
                x = (x + 1) // 2
                x = (x - k) if x >= k else x
                x += dfs(i + 1, a - 1, b - 1)
                res.append(x)

            # op1 -> op2
            if a > 0 and b > 0 and nums[i] >= k:
                x = nums[i]
                x = (x - k) if x >= k else x
                x = (x + 1) // 2
                x += dfs(i + 1, a - 1, b - 1)
                res.append(x)

            return min(res)

        ans = dfs(0, op1, op2)
        return ans


true, false, null = True, False, None
import aatest_helper

cases = [
    aatest_helper.OrderedDict(nums=[2, 8, 3, 19, 3], k=3, op1=1, op2=1, res=23),
    aatest_helper.OrderedDict(nums=[2, 4, 3], k=3, op1=2, op2=1, res=3),
]

aatest_helper.run_test_cases(Solution().minArraySum, cases)

if __name__ == '__main__':
    pass
