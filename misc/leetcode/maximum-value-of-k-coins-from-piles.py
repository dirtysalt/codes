#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def maxValueOfCoins(self, piles: List[List[int]], k: int) -> int:

        import copy
        acc = copy.deepcopy(piles)
        for xs in acc:
            for i in range(1, len(xs)):
                xs[i] += xs[i - 1]

        import functools
        @functools.lru_cache(maxsize=None)
        def search(i, k):
            if i == len(piles):
                return 0
            if k == 0:
                return 0

            ans = search(i + 1, k)
            for j in range(len(piles[i])):
                k2 = k - j - 1
                if k2 < 0:
                    break
                res = acc[i][j]
                res += search(i + 1, k2)
                ans = max(ans, res)
            return ans

        ans = search(0, k)
        return ans


true, false, null = True, False, None
cases = [
    ([[1, 100, 3], [7, 8, 9]], 2, 101),
    ([[100], [100], [100], [100], [100], [100], [1, 1, 1, 1, 1, 1, 700]], 7, 706),
]

import aatest_helper

aatest_helper.run_test_cases(Solution().maxValueOfCoins, cases)

if __name__ == '__main__':
    pass
