#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        def test(x):
            ans = 0
            for y in nums:
                ans += abs(x - y)
            return ans

        nums.sort()
        n = len(nums)
        ans = test(nums[n // 2])
        # 这里很巧妙，为什么可以只选择其中一个呢？
        # if n % 2 == 0:
        #     ans = min(test(nums[n // 2 - 1]), ans)
        return ans


cases = [
    ([1, 2], 1),
    ([1, 0, 0, 8, 6], 14),
    ([1, 2, 3], 2)
]

import aatest_helper

aatest_helper.run_test_cases(Solution().minMoves2, cases)
