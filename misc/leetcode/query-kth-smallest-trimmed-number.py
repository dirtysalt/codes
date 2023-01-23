#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def smallestTrimmedNumbers(self, nums: List[str], queries: List[List[int]]) -> List[int]:

        def value(x):
            r = 0
            for c in x:
                r = r * 10 + ord(c) - ord('0')
            return r

        import functools
        @functools.lru_cache(maxsize=None)
        def get_values(t):
            xs = [(value(x[-t:]), i) for (i, x) in enumerate(nums)]
            xs.sort()
            return xs

        def doquery(k, t):
            xs = get_values(t)
            # print(xs, k)
            return xs[k - 1][1]

        ans = []
        for k, t in queries:
            r = doquery(k, t)
            ans.append(r)

        return ans


true, false, null = True, False, None
cases = [
    (["102", "473", "251", "814"], [[1, 1], [2, 3], [4, 2], [1, 2]], [2, 2, 1, 0]),
    (["24", "37", "96", "04"], [[2, 1], [2, 2]], [3, 0])
]

import aatest_helper

aatest_helper.run_test_cases(Solution().smallestTrimmedNumbers, cases)

if __name__ == '__main__':
    pass
