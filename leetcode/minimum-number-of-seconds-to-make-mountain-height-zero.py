#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def minNumberOfSeconds(self, mountainHeight: int, workerTimes: List[int]) -> int:
        def test(t):
            res = 0
            for w in workerTimes:
                # x*(x+1)*w / 2 <= t
                from math import sqrt
                x = int(sqrt((2 * t) / w))
                x -= 1
                while x * (x + 1) * w <= 2 * t:
                    x += 1
                x -= 1
                res += x
            return res >= mountainHeight

        s, e = 0, (mountainHeight * (mountainHeight + 1)) // 2 * min(workerTimes)
        while s <= e:
            m = (s + e) // 2
            ok = test(m)
            if ok:
                e = m - 1
            else:
                s = m + 1
        return s


true, false, null = True, False, None
import aatest_helper

cases = [
    (5, [3], 45),
    (5, [1], 15),
]

aatest_helper.run_test_cases(Solution().minNumberOfSeconds, cases)

if __name__ == '__main__':
    pass
