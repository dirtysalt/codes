#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def findPaths(self, m: int, n: int, N: int, i: int, j: int) -> int:
        dp = []
        for _ in range(2):
            tmp = []
            for _ in range(m):
                tmp.append([0] * n)
            dp.append(tmp)

        now = 0
        dp[now][i][j] = 1
        P = 10 ** 9 + 7
        ans = 0

        # 这个迭代顺序有点奇怪.
        for _ in range(N):
            ans += sum(dp[now][0][j] for j in range(n))
            ans += sum(dp[now][m - 1][j] for j in range(n))
            ans += sum(dp[now][i][0] for i in range(m))
            ans += sum(dp[now][i][n - 1] for i in range(m))
            ans = ans % P

            for i in range(m):
                for j in range(n):
                    # 这里不能使用前一次的数值，不然会造成重复累计
                    res = 0
                    res += dp[now][i - 1][j] if i > 0 else 0
                    res += dp[now][i + 1][j] if i < (m - 1) else 0
                    res += dp[now][i][j - 1] if j > 0 else 0
                    res += dp[now][i][j + 1] if j < (n - 1) else 0
                    dp[1 - now][i][j] = res % P
            now = 1 - now

        return ans


cases = [
    (2, 2, 2, 0, 0, 6),
    (1, 3, 3, 0, 1, 12)
]

import aatest_helper

aatest_helper.run_test_cases(Solution().findPaths, cases)
