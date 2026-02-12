#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def numberOfComponents(self, properties: List[List[int]], k: int) -> int:
        properties = [set(x) for x in properties]

        def intersect(a, b):
            x = a & b
            return len(x)

        n = len(properties)
        adj = [[] for _ in range(n)]
        for i in range(n):
            for j in range(i + 1, n):
                if intersect(properties[i], properties[j]) >= k:
                    adj[i].append(j)
                    adj[j].append(i)

        # print(adj)
        visited = [0] * n

        def dfs(x, value):
            nonlocal visited
            visited[x] = value
            for y in adj[x]:
                if not visited[y]:
                    dfs(y, value)

        ans = 0
        for i in range(n):
            if not visited[i]:
                ans += 1
                dfs(i, ans)
        return ans


true, false, null = True, False, None
import aatest_helper

cases = [
    aatest_helper.OrderedDict(properties=[[1, 2], [1, 1], [3, 4], [4, 5], [5, 6], [7, 7]], k=1, res=3),
    aatest_helper.OrderedDict(properties=[[1, 2, 3], [2, 3, 4], [4, 3, 5]], k=2, res=1),
    aatest_helper.OrderedDict(properties=[[1, 1], [1, 1]], k=2, res=2),
]

aatest_helper.run_test_cases(Solution().numberOfComponents, cases)

if __name__ == '__main__':
    pass
