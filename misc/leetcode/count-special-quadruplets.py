#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def countQuadruplets(self, nums: List[int]) -> int:
        n = len(nums)

        ans = 0
        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    for d in range(k + 1, n):
                        if (nums[i] + nums[j] + nums[k]) == nums[d]:
                            ans += 1
        return ans


true, false, null = True, False, None
cases = [
    ([28, 8, 49, 85, 37, 90, 20, 8], 1),
]

import aatest_helper

aatest_helper.run_test_cases(Solution().countQuadruplets, cases)

if __name__ == '__main__':
    pass
