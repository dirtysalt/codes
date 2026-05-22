#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def findSubtreeSizes(self, parent: List[int], s: str) -> List[int]:
        n = len(parent)
        ans = [0] * n

        adj = [[] for _ in range(n)]
        for i, p in enumerate(parent):
            if p == -1: continue
            adj[p].append(i)
        st = [[] for _ in range(26)]
        np = parent.copy()

        def dfs(x):
            ans[x] = 1
            c = ord(s[x]) - ord('a')
            st[c].append(x)

            for y in adj[x]:
                dfs(y)
                if np[y] != -1:
                    ans[np[y]] += ans[y]

            st[c].pop()
            if st[c]:
                np[x] = st[c][-1]
            return

        dfs(0)
        # print(np)
        return ans


true, false, null = True, False, None

cases = [
    ([-1, 0, 0, 1, 1, 1], "abaabc", [6, 3, 1, 1, 1, 1]),
    ([-1, 0, 4, 0, 1], "abbba", [5, 2, 1, 1, 1]),
]
import aatest_helper

aatest_helper.run_test_cases(Solution().findSubtreeSizes, cases)

if __name__ == '__main__':
    pass
