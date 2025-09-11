#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def ways(self, pizza: List[str], k: int) -> int:
        K = k - 1
        n, m = len(pizza), len(pizza[0])

        acc = [[0] * (m + 1) for _ in range(n + 1)]
        for i in range(n):
            for j in range(m):
                c = 1 if pizza[i][j] == 'A' else 0
                acc[i + 1][j + 1] = acc[i + 1][j] + c
            for j in range(m):
                acc[i + 1][j + 1] += acc[i][j + 1]
        # print(acc)

        def query(i, j, x, y):
            res = acc[x + 1][y + 1] - acc[i][y + 1] - acc[x + 1][j] + acc[i][j]
            # print('Q {}|{} = {}'.format((i, j), (x, y), res))
            return res

        dp = {}

        def fun(r, c, k):
            if r == n or c == m:
                return 0

            if k == 0:
                res = query(r, c, n - 1, m - 1)
                if res > 0:
                    return 1
                return 0

            key = (r, c, k)
            if key in dp:
                return dp[key]

            ans = 0
            for r2 in range(r, n):
                if query(r, c, r2, m - 1) > 0:
                    ans += fun(r2 + 1, c, k - 1)
            for c2 in range(c, m):
                if query(r, c, n - 1, c2) > 0:
                    ans += fun(r, c2 + 1, k - 1)

            # print(key, ans)
            dp[key] = ans
            return ans

        ans = fun(0, 0, K)
        return ans


cases = [
    (["AAA"], 2, 2),
    (["A..", "AAA", "..."], 3, 3)
]

import aatest_helper

aatest_helper.run_test_cases(Solution().ways, cases)
