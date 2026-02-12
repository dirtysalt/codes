#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def minimumTotalDistance(self, robot: List[int], factory: List[List[int]]) -> int:
        robot.sort()
        factory.sort(key=lambda x: x[0])
        # print(robot, factory)
        INF = 1 << 63

        import functools
        @functools.cache
        def dfs(i, j):
            if i == len(robot): return 0
            if j == len(factory): return INF
            ans = dfs(i, j + 1)
            c = 0
            for d in range(min(factory[j][1], len(robot) - i)):
                c += abs(robot[i + d] - factory[j][0])
                res = dfs(i + d + 1, j + 1)
                ans = min(ans, c + res)
            return ans

        ans = dfs(0, 0)
        return ans


true, false, null = True, False, None
cases = [
    ([0, 4, 6], [[2, 2], [6, 2]], 4),
    ([1, -1], [[-2, 1], [2, 1]], 2),
    ([9, 11, 99, 101], [[10, 1], [7, 1], [14, 1], [100, 1], [96, 1], [103, 1]], 6),
]

import aatest_helper

aatest_helper.run_test_cases(Solution().minimumTotalDistance, cases)

if __name__ == '__main__':
    pass
