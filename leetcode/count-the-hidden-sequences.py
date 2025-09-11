#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
        s, e = lower, upper
        for x in differences:
            s2, e2 = lower - x, upper - x
            s, e = max(s, s2), min(e, e2)
            s, e = s + x, e + x
        ans = max(0, e - s + 1)
        return ans


true, false, null = True, False, None
cases = [
    ([1, -3, 4], 1, 6, 2),
    ([3, -4, 5, 1, -2], -4, 5, 4),
    ([4, -7, 2], 3, 6, 0),
    ([-36115], 50665, 89472, 2693),
]

import aatest_helper

aatest_helper.run_test_cases(Solution().numberOfArrays, cases)

if __name__ == '__main__':
    pass
