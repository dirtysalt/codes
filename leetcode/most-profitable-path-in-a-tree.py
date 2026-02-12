#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def mostProfitablePath(self, edges: List[List[int]], bob: int, amount: List[int]) -> int:
        n = len(edges) + 1
        adj = [[] for _ in range(n)]

        for x, y in edges:
            adj[x].append(y)
            adj[y].append(x)

        def dfsb(x, p, path):
            if x == 0:
                return True
            for y in adj[x]:
                if y == p: continue
                path.append(y)
                if dfsb(y, x, path): return True
                path.pop()
            return False

        pathb = [bob]
        dfsb(bob, -1, pathb)
        # print(pathb)
        INF = 1 << 63

        def compute(pa, pb):
            a = 0
            # print(pa, pb)
            visited = set()
            for x, y in zip(pa, pb):
                c = amount[x]
                if x not in visited:
                    if x == y:
                        a += c // 2
                    else:
                        a += c
                visited.add(x)
                visited.add(y)
            m = min(len(pa), len(pb))
            for i in range(m, len(pa)):
                x = pa[i]
                c = amount[x]
                if x not in visited:
                    a += c
            return a

        def dfsa(x, p, path):
            if x != 0 and len(adj[x]) == 1:
                # leaf node.
                res = compute(path, pathb)
                return res

            ans = -INF
            for y in adj[x]:
                if y == p: continue
                path.append(y)
                res = dfsa(y, x, path)
                ans = max(ans, res)
                path.pop()

            return ans

        path = [0]
        ans = dfsa(0, -1, path)
        return ans


true, false, null = True, False, None
cases = [
    ([[0, 1], [1, 2], [1, 3], [3, 4]], 3, [-2, 4, 2, -4, 6], 6),
    ([[0, 1]], 1, [-7280, 2350], -7280),
]

import aatest_helper

aatest_helper.run_test_cases(Solution().mostProfitablePath, cases)

if __name__ == '__main__':
    pass
