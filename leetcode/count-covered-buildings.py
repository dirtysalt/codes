#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def countCoveredBuildings(self, n: int, buildings: List[List[int]]) -> int:
        from collections import Counter, defaultdict
        cnt = Counter()

        xs = defaultdict(list)
        ys = defaultdict(list)
        for x, y in buildings:
            xs[x].append(y)
            ys[y].append(x)

        for x in xs.keys():
            y = xs[x]
            y.sort()
            for i in range(1, len(y) - 1):
                cnt[(x, y[i])] += 1

        for y in ys.keys():
            x = ys[y]
            x.sort()
            for i in range(1, len(x) - 1):
                cnt[(x[i], y)] += 1

        ans = 0
        for _, v in cnt.items():
            if v == 2:
                ans += 1
        return ans


true, false, null = True, False, None
import aatest_helper

cases = [
    (3, [[1, 2], [2, 2], [3, 2], [2, 1], [2, 3]], 1),
    (3, [[1, 1], [1, 2], [2, 1], [2, 2]], 0),
    (5, [[1, 3], [3, 2], [3, 3], [3, 5], [5, 3]], 1),
]

aatest_helper.run_test_cases(Solution().countCoveredBuildings, cases)

if __name__ == '__main__':
    pass
