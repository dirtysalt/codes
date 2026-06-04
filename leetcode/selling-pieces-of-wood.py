#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def sellingWood(self, m: int, n: int, prices: List[List[int]]) -> int:

        import collections
        hs = collections.defaultdict(list)
        ws = collections.defaultdict(list)
        for h, w, p in prices:
            hs[h].append((w, p))
            ws[w].append((h, p))
        hkeys = sorted(hs.keys())
        wkeys = sorted(ws.keys())
        for xs in hs.values():
            xs.sort()
        for xs in ws.values():
            xs.sort()

        besth = collections.defaultdict(lambda: [0] * (n + 1))
        bestw = collections.defaultdict(lambda: [0] * (m + 1))
        for h in hs.keys():
            dp = besth[h]
            for j in range(n):
                for w, p in hs[h]:
                    if (j + w) > n: break
                    dp[j + w] = max(dp[j + w], dp[j] + p)
                dp[j + 1] = max(dp[j], dp[j + 1])

        for w in ws.keys():
            dp = bestw[w]
            for i in range(m):
                for h, p in ws[w]:
                    if (i + h) > m: break
                    dp[i + h] = max(dp[i + h], dp[i] + p)
                dp[i + 1] = max(dp[i], dp[i + 1])

        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(m):
            for j in range(n):
                for h in hkeys:
                    if (i + h) > m: break
                    t = besth[h][n - j]
                    dp[i + h][j] = max(dp[i + h][j], dp[i][j] + t)
                for w in wkeys:
                    if (j + w) > n: break
                    t = bestw[w][m - i]
                    dp[i][j + w] = max(dp[i][j + w], dp[i][j] + t)

        ans = 0
        for i in range(m):
            ans = max(ans, max(dp[i]))
        return ans


true, false, null = True, False, None
cases = [
    (3, 5, [[1, 4, 2], [2, 2, 7], [2, 1, 3]], 19),
    (4, 6, [[3, 2, 10], [1, 4, 2], [4, 1, 3]], 32),
    (9, 7, [[4, 3, 2], [5, 3, 16], [4, 4, 18], [8, 7, 6]], 54),
]

import aatest_helper

aatest_helper.run_test_cases(Solution().sellingWood, cases)

if __name__ == '__main__':
    pass
