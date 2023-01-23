#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        adj = [[] for _ in range(n)]
        ind = [0] * n
        for x, y in relations:
            x, y = x - 1, y - 1
            adj[x].append(y)
            ind[y] += 1

        finish = [0] * n
        import heapq
        dq = []
        for x in range(n):
            if ind[x] == 0:
                finish[x] = time[x]
                heapq.heappush(dq, (finish[x], x))

        while dq:
            t, x = heapq.heappop(dq)
            for y in adj[x]:
                ind[y] -= 1
                if ind[y] == 0:
                    finish[y] = t + time[y]
                    heapq.heappush(dq, (finish[y], y))

        return max(finish)


true, false, null = True, False, None
cases = [
    (3, [[1, 3], [2, 3]], [3, 2, 5], 8),
    (5, [[1, 5], [2, 5], [3, 5], [3, 4], [4, 5]], [1, 2, 3, 4, 5], 12),
]

import aatest_helper

aatest_helper.run_test_cases(Solution().minimumTime, cases)

if __name__ == '__main__':
    pass
