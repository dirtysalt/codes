#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt
from collections import OrderedDict
from typing import List


class Solution:
    def minSizeSubarray(self, nums: List[int], target: int) -> int:
        INF = (1 << 63)
        ans = INF

        pos = {0: 0}
        total = 0
        for i in range(len(nums)):
            total += nums[i]
            pos[total] = i + 1
            if (total - target) in pos:
                ans = min(ans, i + 1 - pos[total - target])

        c = total
        for i in range(len(nums)):
            t = (target - c)
            if t >= 0 and (t % total) in pos:
                end = pos[t % total]
                r = len(nums) - i + (t // total) * len(nums) + end
                # print(r, nums[i:] + (nums) * (t // total) + nums[:end])
                ans = min(ans, r)
            c -= nums[i]

        if ans == INF:
            ans = -1
        return ans


true, false, null = True, False, None
import aatest_helper

cases = [
    OrderedDict(nums=[1, 2, 3], target=5, res=2),
    OrderedDict(nums=[1, 1, 1, 2, 3], target=4, res=2),
    OrderedDict(nums=[2, 4, 6, 8], target=3, res=-1),
    ([18, 3, 11, 19, 7, 16, 6, 7, 3, 6, 18, 9, 9, 1, 14, 17, 15, 14, 12, 10], 7, 1),
    ([1, 2, 2, 2, 1, 2, 1, 2, 1, 2, 1], 83, 53),
]

aatest_helper.run_test_cases(Solution().minSizeSubarray, cases)

if __name__ == '__main__':
    pass
