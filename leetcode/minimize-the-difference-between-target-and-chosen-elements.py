#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def minimizeTheDifference(self, mat: List[List[int]], target: int) -> int:
        dp = [set(), set()]
        now = 0
        dp[now].add(0)

        n, m = len(mat), len(mat[0])

        for i in range(n):
            dp[1 - now] = set()
            for j in range(m):
                for x in dp[now]:
                    z = x + mat[i][j]
                    if z > 2 * target: continue
                    dp[1 - now].add(z)
            now = 1 - now

        if len(dp[now]) == 0:
            ans = 0
            for i in range(n):
                ans += min(mat[i])
            ans = abs(ans - target)
            return ans

        ans = 1 << 30
        for x in dp[now]:
            diff = abs(x - target)
            if diff < ans:
                ans = diff
        return ans


true, false, null = True, False, None
cases = [
    ([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 13, 0),
    ([[1], [2], [3]], 100, 94),
    ([[1, 2, 9, 8, 7]], 6, 1),
]

import aatest_helper

aatest_helper.run_test_cases(Solution().minimizeTheDifference, cases)

if __name__ == '__main__':
    pass
