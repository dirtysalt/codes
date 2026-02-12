#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def maxPossibleScore(self, start: List[int], d: int) -> int:
        start.sort()

        def test(k):
            last = start[0]
            for x in start[1:]:
                last += k
                if last > x + d: return False
                last = max(last, x)
            return True

        e = max([start[i] - start[i - 1] for i in range(1, len(start))]) + d
        s = 0
        while s <= e:
            m = (s + e) // 2
            ok = test(m)
            if ok:
                s = m + 1
            else:
                e = m - 1
        return e


true, false, null = True, False, None
import aatest_helper

cases = [
    ([6, 0, 3], 2, 4),
    ([2, 6, 13, 13], 5, 5),
    ([0, 9, 2, 9], 2, 2),
]

aatest_helper.run_test_cases(Solution().maxPossibleScore, cases)

if __name__ == '__main__':
    pass
