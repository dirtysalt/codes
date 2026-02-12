#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        def split2(x):
            r = min(limit, x) - max(x - limit, 0) + 1
            return max(r, 0)

        ans = 0
        for i in range(0, min(limit, n) + 1):
            x = n - i
            r = split2(x)
            ans += r
        return ans


true, false, null = True, False, None
import aatest_helper

cases = [
    (5, 2, 3,),
    (3, 3, 10),
    (4, 1, 0),
]

aatest_helper.run_test_cases(Solution().distributeCandies, cases)

if __name__ == '__main__':
    pass
