#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt


class Solution:
    def minEnd(self, n: int, x: int) -> int:
        n -= 1

        ans = x
        j = 0
        while n:
            while x & (1 << j):
                j += 1
            if n & 0x1:
                ans |= (1 << j)
            n = n >> 1
            j += 1
        return ans


true, false, null = True, False, None
import aatest_helper

cases = [
    (3, 4, 6),
    (2, 7, 15),
]

aatest_helper.run_test_cases(Solution().minEnd, cases)

if __name__ == '__main__':
    pass
