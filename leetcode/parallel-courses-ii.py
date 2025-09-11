#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def minNumberOfSemesters(self, n: int, dependencies: List[List[int]], k: int) -> int:
        inf = 999
        ST = 1 << n
        dp = [inf] * ST
        radj = [[] for _ in range(n)]
        for x, y in dependencies:
            radj[y - 1].append(x - 1)

        def walk(cs, k):
            off = len(cs) - k
            base = 0
            for x in cs:
                base = base | (1 << x)

            if off <= 0:
                yield base

            else:
                import itertools
                for xs in itertools.combinations(cs, off):
                    st = base
                    for x in xs:
                        st = st & ~(1 << x)
                    yield st

        dp[0] = 0
        for st in range(ST):
            # find possible courses.
            cs = []
            for x in range(n):
                if st & (1 << x): continue
                ok = True
                for y in radj[x]:
                    if (st & (1 << y)) == 0:
                        ok = False
                if ok:
                    cs.append(x)

            # enumerate possible combinations.
            for st2 in walk(cs, k):
                st3 = st | st2
                dp[st3] = min(dp[st3], dp[st] + 1)

        ans = dp[-1]
        return ans


cases = [
    (1, [], 1, 1),
    (2, [[1, 2]], 2, 2),
    (4, [[2, 1], [3, 1], [1, 4]], 2, 3),
    (12, [[1, 2], [1, 3], [7, 5], [7, 6], [4, 8], [8, 9], [9, 10], [10, 11], [11, 12]], 2, 6),
    (11, [], 2, 6)
]
import aatest_helper

aatest_helper.run_test_cases(Solution().minNumberOfSemesters, cases)
