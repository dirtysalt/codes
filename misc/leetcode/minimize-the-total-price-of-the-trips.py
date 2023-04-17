#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def minimumTotalPrice(self, n: int, edges: List[List[int]], price: List[int], trips: List[List[int]]) -> int:
        count = [0] * n
        adj = [[] for _ in range(n)]
        for x, y in edges:
            adj[x].append(y)
            adj[y].append(x)

        def visit(start, end):
            def dfs(x, p):
                if x == end:
                    count[x] += 1
                    return True
                for y in adj[x]:
                    if y == p: continue
                    ret = dfs(y, x)
                    if ret:
                        count[x] += 1
                        return ret
                return False

            ret = dfs(start, -1)
            assert ret

        for start, end in trips:
            visit(start, end)

        # search nodes to cut half.
        import functools
        @functools.cache
        def search(x, p, pused):
            # don't cut x
            ans = 0
            for y in adj[x]:
                if y == p: continue
                ans += search(y, x, False)

            if not pused:
                r = count[x] * (price[x] // 2)
                for y in adj[x]:
                    if y == p: continue
                    r += search(y, x, True)
                ans = max(ans, r)
            return ans

        A, M = 0, 0
        for x in range(n):
            A += count[x] * price[x]
            r = search(x, -1, False)
            M = max(M, r)
        return A - M


true, false, null = True, False, None
import aatest_helper

cases = [
    (4, [[0, 1], [1, 2], [1, 3]], [2, 2, 10, 6], [[0, 3], [2, 1], [2, 3]], 23),
    (2, [[0, 1]], [2, 2], [[0, 0]], 1),
]

aatest_helper.run_test_cases(Solution().minimumTotalPrice, cases)

if __name__ == '__main__':
    pass
