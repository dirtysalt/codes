#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        from collections import defaultdict
        meets = defaultdict(list)
        times = set()
        for x, y, t in meetings:
            meets[t].append((x, y))
            times.add(t)
        times = list(times)
        times.sort()

        ans = set()
        ans.add(0)
        ans.add(firstPerson)

        for t in times:
            adj = defaultdict(list)
            pp = set()
            for x, y in meets[t]:
                adj[x].append(y)
                adj[y].append(x)
                pp.add(x)
                pp.add(y)

            def dfs(u):
                for v in adj[u]:
                    if v in ans: continue
                    ans.add(v)
                    dfs(v)

            for u in pp:
                if u in ans:
                    dfs(u)

        ans = list(ans)
        ans.sort()
        return ans


true, false, null = True, False, None
cases = [
    (6, [[1, 2, 5], [2, 3, 8], [1, 5, 10]], 1, [0, 1, 2, 3, 5]),
    (4, [[3, 1, 3], [1, 2, 2], [0, 3, 3]], 3, [0, 1, 3]),
    (5, [[3, 4, 2], [1, 2, 1], [2, 3, 1]], 1, [0, 1, 2, 3, 4]),
    (6, [[0, 2, 1], [1, 3, 1], [4, 5, 1]], 1, [0, 1, 2, 3]),
]

import aatest_helper

aatest_helper.run_test_cases(Solution().findAllPeople, cases)

if __name__ == '__main__':
    pass
