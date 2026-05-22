#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        from sortedcontainers import SortedList
        sl = SortedList(list(range(n)))
        ans = []
        for x, y in queries:
            i = sl.bisect_left(x)
            if 0 <= i < len(sl) - 1 and sl[i] == x:
                j = sl.bisect_left(y)
                values = [sl[k] for k in range(i + 1, j)]
                for v in values:
                    sl.remove(v)
            ans.append(len(sl) - 1)
        return ans


true, false, null = True, False, None
import aatest_helper

cases = [
    (5, [[2, 4], [0, 2], [0, 4]], [3, 2, 1]),
    (4, [[0, 3], [0, 2]], [1, 1, ]),
]

aatest_helper.run_test_cases(Solution().shortestDistanceAfterQueries, cases)

if __name__ == '__main__':
    pass
