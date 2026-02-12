#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List

from sortedcontainers import SortedList


class Solution:
    def recoverArray(self, nums: List[int]) -> List[int]:
        nums.sort()
        n = len(nums)

        ans = []

        def check(k):
            ans.clear()
            sl = SortedList(nums)
            while sl:
                x = sl.pop(0)
                ans.append(x + k)
                exp = x + 2 * k
                if exp not in sl:
                    return False
                sl.remove(exp)
            return True

        for i in range(1, n // 2 + 1):
            k = nums[i] - nums[0]
            if k > 0 and k % 2 == 0 and check(k // 2):
                return ans


true, false, null = True, False, None
cases = [
    ([2, 10, 6, 4, 8, 12], [3, 7, 11]),
    ([1, 1, 3, 3], [2, 2]),
    ([5, 435], [220]),
]

import aatest_helper

aatest_helper.run_test_cases(Solution().recoverArray, cases)

if __name__ == '__main__':
    pass
