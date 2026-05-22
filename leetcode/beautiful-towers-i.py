#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def maximumSumOfHeights(self, maxHeights: List[int]) -> int:
        hs = maxHeights

        def fit(k):
            ans = hs[k]

            last = hs[k]
            for i in reversed(range(k)):
                last = min(last, hs[i])
                ans += last
            last = hs[k]
            for i in range(k + 1, len(hs)):
                last = min(last, hs[i])
                ans += last

            return ans

        ans = 0
        for k in range(len(hs)):
            c = fit(k)
            ans = max(ans, c)
        return ans


true, false, null = True, False, None
import aatest_helper

cases = [
    ([5, 3, 4, 1, 1], 13),
    ([6, 5, 3, 9, 2, 7], 22),
    ([3, 2, 5, 5, 2, 3], 18),
]

aatest_helper.run_test_cases(Solution().maximumSumOfHeights, cases)

if __name__ == '__main__':
    pass
