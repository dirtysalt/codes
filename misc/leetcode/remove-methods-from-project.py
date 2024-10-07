#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def remainingMethods(self, n: int, k: int, invocations: List[List[int]]) -> List[int]:
        called = [[] for _ in range(n)]
        caller = [[] for _ in range(n)]
        for a, b in invocations:
            called[a].append(b)
            caller[b].append(a)

        sus = set()

        def mark_sus(x):
            sus.add(x)
            for y in called[x]:
                if y not in sus:
                    mark_sus(y)

        mark_sus(k)

        used = set()

        def mark_used(x):
            used.add(x)
            for y in called[x]:
                if y not in used:
                    mark_used(y)
            for y in caller[x]:
                if y not in used:
                    mark_used(y)

        starts = [x for x in range(n) if x not in sus]
        for p in starts:
            mark_used(p)

        ans = sorted(list(used))
        return ans


true, false, null = True, False, None
import aatest_helper

cases = [
    aatest_helper.OrderedDict(n=4, k=1, invocations=[[1, 2], [0, 1], [3, 2]], res=[0, 1, 2, 3]),
    aatest_helper.OrderedDict(n=5, k=0, invocations=[[1, 2], [0, 2], [0, 1], [3, 4]], res=[3, 4]),
    aatest_helper.OrderedDict(n=3, k=2, invocations=[[1, 2], [0, 1], [2, 0]], res=[]),
    (3, 2, [[1, 0], [2, 0]], [0, 1, 2]),
]

aatest_helper.run_test_cases(Solution().remainingMethods, cases)

if __name__ == '__main__':
    pass
