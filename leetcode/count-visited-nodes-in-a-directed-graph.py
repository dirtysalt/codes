#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def countVisitedNodes(self, edges: List[int]) -> List[int]:
        n = len(edges)
        ans = [-1] * n

        visited = [0] * n

        def findCircle(x):
            pos = {}
            idx = 0
            while not visited[x]:
                visited[x] = 1
                pos[x] = idx
                x = edges[x]
                idx += 1
            if x not in pos:
                return
            size = idx - pos[x]
            for _ in range(size):
                ans[x] = size
                x = edges[x]

        for i in range(n):
            findCircle(i)

        # print(ans)

        def dfs(x):
            path = []
            while ans[x] == -1:
                path.append(x)
                x = edges[x]
            for i in range(len(path)):
                ans[path[i]] = len(path) - i + ans[x]

        for i in range(n):
            dfs(i)

        return ans


true, false, null = True, False, None
import aatest_helper

cases = [
    aatest_helper.OrderedDict(edges=[1, 2, 0, 0], res=[3, 3, 3, 4]),
    aatest_helper.OrderedDict(edges=[1, 2, 3, 4, 0], res=[5, 5, 5, 5, 5]),
]

aatest_helper.run_test_cases(Solution().countVisitedNodes, cases)

if __name__ == '__main__':
    pass
