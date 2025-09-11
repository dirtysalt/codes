#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def checkIfPrerequisite(self, n: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        adj = [[] for _ in range(n)]
        ind = [0] * n
        for a, b in prerequisites:
            adj[a].append(b)
            ind[b] += 1

        from collections import deque
        dq = deque()
        for i in range(n):
            if ind[i] == 0:
                dq.append(i)

        ps = [set([i]) for i in range(n)]
        while dq:
            x = dq.popleft()
            for y in adj[x]:
                ind[y] -= 1
                ps[y] |= ps[x]
                if ind[y] == 0:
                    dq.append(y)

        # print(ps)
        ans = []
        for a, b in queries:
            ans.append(a in ps[b])
        return ans


true = True
false = False
cases = [
    (2, [[1, 0]], [[0, 1], [1, 0]], [false, true]),
    (5, [[0, 1], [1, 2], [2, 3], [3, 4]], [[0, 4], [4, 0], [1, 3], [3, 0]], [true, false, true, false]),
]

import aatest_helper

aatest_helper.run_test_cases(Solution().checkIfPrerequisite, cases)
