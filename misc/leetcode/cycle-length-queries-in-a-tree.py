#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def cycleLengthQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        def handleQuery(x, y):
            path = {}
            dist = 1
            while x != 0:
                path[x] = dist
                x = x // 2
                dist += 1

            d = 1
            while y != 0:
                if y in path:
                    dist = path[y]
                    return d + dist - 1
                else:
                    y = y // 2
                    d += 1

        ans = []
        for x, y in queries:
            res = handleQuery(x, y)
            ans.append(res)
        return ans


true, false, null = True, False, None
import aatest_helper

cases = [
    (3, [[5, 3], [4, 7], [2, 3]], [4, 5, 3]),
    (2, [[1, 2]], [2]),
]

aatest_helper.run_test_cases(Solution().cycleLengthQueries, cases)

if __name__ == '__main__':
    pass
