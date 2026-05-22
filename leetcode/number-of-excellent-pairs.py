#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def countExcellentPairs(self, nums: List[int], k: int) -> int:
        nums = list(set(nums))

        def bits(x):
            t = 0
            while x:
                if x & 0x1: t += 1
                x = x >> 1
            return t

        count = [0] * 32
        for x in nums:
            b = bits(x)
            count[b] += 1

        ans = 0
        for x in nums:
            b = bits(x)
            for i in range(max(0, k - b), 32):
                if count[i]:
                    # print(x, i, count[i])
                    ans += count[i]

        return ans


true, false, null = True, False, None
cases = [
    ([1, 2, 3, 1], 3, 5),
    ([5, 1, 1], 10, 0),
]

import aatest_helper

aatest_helper.run_test_cases(Solution().countExcellentPairs, cases)

if __name__ == '__main__':
    pass
