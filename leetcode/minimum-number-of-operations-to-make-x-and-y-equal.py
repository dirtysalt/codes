#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def minimumOperationsToMakeEqual(self, x: int, y: int) -> int:
        import heapq

        target = x
        N = 10**4

        PQ = []
        PQ.append((0, y))
        dp = [-1] * (N + 1)

        def add_edge(cost, x):
            if 0 <= x <= N and (dp[x] == -1 or dp[x] > cost):
                dp[x] = cost
                heapq.heappush(PQ, (cost, x))

        while PQ:
            (d, x) = heapq.heappop(PQ)
            if x == target:
                return d
            # x-1, x * 11, x * 5, x + 1
            add_edge(d + 1, x - 1)
            if x * 11 > target:
                add_edge(d + 1 + x * 11 - target, target)
            else:
                add_edge(d + 1, x * 11)
            if x * 5 > target:
                add_edge(d + 1 + x * 5 - target, target)
            else:
                add_edge(d + 1, x * 5)
            add_edge(d + 1, x + 1)


true, false, null = True, False, None
import aatest_helper

cases = [
    (26, 1, 3),
    (54, 2, 4),
    (25, 30, 5),
    (5, 2, 2),
]

aatest_helper.run_test_cases(Solution().minimumOperationsToMakeEqual, cases)

if __name__ == '__main__':
    pass
