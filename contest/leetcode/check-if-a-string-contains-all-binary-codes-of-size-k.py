#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        n = len(s)
        j = 0
        x = 0
        nums = set()
        for i in range(n):
            x = x * 2 + int(s[i])
            if (i - j + 1) > k:
                x -= int(s[j]) * (1 << k)
                j += 1
            if (i - j + 1) == k:
                nums.add(x)
        return len(nums) == (1 << k)


cases = [
    ("00110110", 2, True),
    ("0000000001011100", 4, False),
    ("0110", 2, False),
    ("0110", 1, True),
]
import aatest_helper

aatest_helper.run_test_cases(Solution().hasAllCodes, cases)
