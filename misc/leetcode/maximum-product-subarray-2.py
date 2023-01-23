#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        _max, _min = 1, 1
        ans = nums[0]

        for x in nums:
            a = _max * x
            b = _min * x
            _max = max(a, b)
            _min = min(a, b)
            # print('>>>', _max, _min)
            ans = max(ans, _max)

            if _max <= 0:
                _max = 1
            if _min == 0:
                _min = 1
            # print('<<<', _max, _min)
        return ans


cases = [
    ([2, 3, -2, 4], 6),
    ([-2, 0, -1], 0),
    ([3, -1, 4], 4),
    ([-4, -3, -2], 12)
]

import aatest_helper

aatest_helper.run_test_cases(Solution().maxProduct, cases)
