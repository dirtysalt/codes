#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def maximumXOR(self, nums: List[int]) -> int:
        cnt = [0] * 32
        bits = 32
        for x in nums:
            for i in range(bits):
                if x & (1 << i):
                    cnt[i] += 1

        ans = 0
        for i in range(bits):
            if cnt[i] >= 1:
                ans = ans | (1 << i)
        return ans


true, false, null = True, False, None
cases = [
    ([3, 2, 4, 6], 7),
    ([1, 2, 3, 9, 2], 11),
]

import aatest_helper

aatest_helper.run_test_cases(Solution().maximumXOR, cases)

if __name__ == '__main__':
    pass
