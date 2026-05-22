#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        tmp = []
        for i in range(n):
            if nums[i] % 2 == 1:
                tmp.append(i)

        ans = 0
        for i in range(len(tmp)):
            j = k + i - 1
            if j >= len(tmp):
                break

            left = tmp[i] - (tmp[i-1] if i > 0 else -1)
            right = (tmp[j+1] if (j+1) < len(tmp) else n) - tmp[j]
            ans += left * right
        return ans


import aatest_helper

cases = [
    ([1, 1, 2, 1, 1],  3, 2),
    ([2, 2, 2, 1, 2, 2, 1, 2, 2, 2],  2, 16),


]

aatest_helper.run_test_cases(Solution().numberOfSubarrays, cases)
