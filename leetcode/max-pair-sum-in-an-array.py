#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def maxSum(self, nums: List[int]) -> int:
        def maxdigit(x):
            res = 0
            while x:
                res = max(res, x % 10)
                x = x // 10
            return res

        n = len(nums)
        ans = -1
        for i in range(n):
            d0 = maxdigit(nums[i])
            for j in range(i + 1, n):
                d1 = maxdigit(nums[j])
                if d0 == d1:
                    ans = max(ans, nums[i] + nums[j])
        return ans


if __name__ == '__main__':
    pass
