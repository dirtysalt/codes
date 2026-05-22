#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt
from typing import List


class Solution:
    def maximumInvitations(self, favorite: List[int]) -> int:
        n = len(favorite)

        def check_cycle():
            cycle = [0] * n
            res = 0
            for i in range(n):
                path, step, buf = {}, 0, []
                x = i
                while x not in path:
                    if cycle[x]: break
                    buf.append(x)
                    path[x] = step
                    step += 1
                    x = favorite[x]

                if cycle[x]:
                    d = cycle[x]
                else:
                    d = step - path[x]

                for x in buf:
                    cycle[x] = d
                res = max(res, d)
            return res

        cycle_size = check_cycle()

        deg = [0] * n
        dp = [1] * n
        from collections import deque
        Q = deque()
        for i in range(n):
            deg[favorite[i]] += 1
        for i in range(n):
            if deg[i] == 0:
                Q.append(i)

        while Q:
            x = Q.popleft()
            to = favorite[x]
            dp[to] = max(dp[to], dp[x] + 1)
            deg[to] -= 1
            if deg[to] == 0:
                Q.append(to)

        concat_size = 0
        for i in range(n):
            if favorite[favorite[i]] == i and i < favorite[i]:
                concat_size += dp[i] + dp[favorite[i]]

        ans = max(cycle_size, concat_size)
        return ans


true, false, null = True, False, None
cases = [
    ([2, 2, 1, 2], 3),
    ([1, 2, 0], 3),
    ([3, 0, 1, 4, 1], 4),
    ([1, 0, 0, 2, 1, 4, 7, 8, 9, 6, 7, 10, 8], 6),
    ([1, 0, 3, 2, 5, 6, 7, 4, 9, 8, 11, 10, 11, 12, 10], 11)
]

import aatest_helper

aatest_helper.run_test_cases(Solution().maximumInvitations, cases)

if __name__ == '__main__':
    pass
