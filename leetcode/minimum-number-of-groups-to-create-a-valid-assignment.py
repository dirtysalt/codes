#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def minGroupsForValidAssignment(self, nums: List[int]) -> int:
        from collections import Counter
        cnt = Counter(nums)
        values = list(cnt.values())
        values.sort()

        def test(x, g):
            r = x % (g + 1)
            c = x // (g + 1)
            if r == 0: return c
            r = (g + 1) * (c + 1) - x
            if r <= (c + 1): return c + 1
            return 0

        for g in reversed(range(1, values[0] + 1)):
            ans = 0
            ok = True
            for x in values:
                c = test(x, g)
                if c == 0:
                    ok = False
                    break
                ans += c
            if ok:
                return ans


true, false, null = True, False, None
import aatest_helper

cases = [
    ([3, 2, 3, 2, 3], 2),
    ([10, 10, 10, 3, 1, 1], 4),
    ([1, 7, 10], 3),
    ([2, 1, 1, 1, 2, 1, 2, 1, 3, 3, 3, 2, 1, 3, 3], 6),
    ([1, 1, 1, 1, 1], 1)
]

aatest_helper.run_test_cases(Solution().minGroupsForValidAssignment, cases)

if __name__ == '__main__':
    pass
