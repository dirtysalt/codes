#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def minimalKSum(self, nums: List[int], k: int) -> int:
        nums.sort()

        last = 1
        ans = 0
        for x in nums:
            # duplicated.
            if x < last:
                continue

            if x != last:
                num = min(x - last, k)
                k -= num
                ans += (last + last + num - 1) * num // 2
            last = x + 1
            if k == 0:
                break

        if k != 0:
            ans += (last + last + k - 1) * k // 2

        return ans


true, false, null = True, False, None
cases = [
    ([1, 4, 25, 10, 25], 2, 5),
    ([5, 6], 6, 25),
    ([96, 44, 99, 25, 61, 84, 88, 18, 19, 33, 60, 86, 52, 19, 32, 47, 35, 50, 94, 17, 29, 98, 22, 21, 72, 100, 40, 84],
     35, 794),
]

import aatest_helper

aatest_helper.run_test_cases(Solution().minimalKSum, cases)

if __name__ == '__main__':
    pass
