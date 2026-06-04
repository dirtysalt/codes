#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        M = max(nums)
        pos = [-1]
        for i in range(len(nums)):
            if nums[i] == M:
                pos.append(i)
        # pos.append(len(nums))

        ans = 0
        for i in range(1, len(pos) - k + 1):
            j = i + k - 1
            x = pos[i] - pos[i - 1]
            y = len(nums) - pos[j]

            # print(x, y)
            ans += x * y
        return ans


true, false, null = True, False, None
import aatest_helper

cases = [
    aatest_helper.OrderedDict(nums=[1, 3, 2, 3, 3], k=2, res=6),
    aatest_helper.OrderedDict(nums=[1, 4, 2, 1], k=3, res=0),
]

aatest_helper.run_test_cases(Solution().countSubarrays, cases)

if __name__ == '__main__':
    pass
