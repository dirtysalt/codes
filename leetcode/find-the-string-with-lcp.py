#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def findTheString(self, lcp: List[List[int]]) -> str:
        n = len(lcp)
        # quick check and build graph
        grid = [[] * n for _ in range(n)]
        for i in range(n):
            if lcp[i][i] != (n - i):
                return ''
            for j in range(i + 1, n):
                if lcp[i][j] != lcp[j][i]:
                    return ''
                d = lcp[i][j]
                if d > (n - max(i, j)):
                    return ''
                if d > 0:
                    if (j + 1) < n and lcp[i + 1][j + 1] != (d - 1):
                        return ''
                    grid[i].append(j)
                    grid[j].append(i)

        # dfs and build connected graph.
        ts = [0] * n

        def dfs(x, now):
            if ts[x] != 0:
                return ts[x] == now
            ts[x] = now
            for y in grid[x]:
                if not dfs(y, now):
                    return False
            return True

        now = 1
        for i in range(n):
            if ts[i]: continue
            # too much connected graphs.
            if now > 26: return ''
            if not dfs(i, now):
                return ''
            now += 1

        ans = [''] * n
        for i in range(n):
            ans[i] = chr(ord('a') + ts[i] - 1)
        ans = ''.join(ans)

        # double check because we only looks for positive requirements.
        # we need to take care of negative requirements.
        for i in range(n):
            for j in range(i + 1, n):
                if lcp[i][j] == 0 and ans[i] == ans[j]:
                    return ''

        return ans


class Solution:
    def findTheString(self, lcp: List[List[int]]) -> str:
        n = len(lcp)
        ans = [''] * n

        # construct loosely answer.
        import string
        i = 0
        for c in string.ascii_lowercase:
            while i < n and ans[i] != '': i += 1
            if i == n: break
            for j in range(i, n):
                if lcp[i][j]: ans[j] = c
        if '' in ans: return ''

        for i in reversed(range(n)):
            for j in reversed(range(i, n)):
                if lcp[i][j] != lcp[j][i]: return ''
                value = 0
                if ans[i] == ans[j]:
                    value = lcp[i + 1][j + 1] if (j + 1) < n else 0
                    value += 1
                if lcp[i][j] != value:
                    return ''

        return ''.join(ans)


true, false, null = True, False, None
import aatest_helper

cases = [
    ([[4, 0, 2, 0], [0, 3, 0, 1], [2, 0, 2, 0], [0, 1, 0, 1]], "abab",),
    ([[4, 3, 2, 1], [3, 3, 2, 1], [2, 2, 2, 1], [1, 1, 1, 1]], "aaaa"),
    ([[4, 3, 2, 1], [3, 3, 2, 1], [2, 2, 2, 1], [1, 1, 1, 3]], ""),
    ([[4, 1, 1, 1], [1, 3, 1, 1], [1, 1, 2, 1], [1, 1, 1, 1]], ""),
    ([[27, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
      [0, 26, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
      [0, 0, 25, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 24, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 23, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 22, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 21, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 20, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 0, 19, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 0, 0, 18, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 17, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 16, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 15, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 14, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 13, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 12, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 11, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 10, 0, 0, 0, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9, 0, 0, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8, 0, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 6, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0],
      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]], ""),
    ([[3, 0, 1], [0, 2, 1], [1, 1, 1]], ""),
]

aatest_helper.run_test_cases(Solution().findTheString, cases)

if __name__ == '__main__':
    pass
