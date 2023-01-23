#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
        n = len(mat)
        m = len(mat[0])

        if n > m:
            n, m = m, n
            mat = list(zip(*mat))

        dp = [[0] * m for _ in range(n + 1)]
        for i in range(n):
            for j in range(m):
                dp[i + 1][j] = dp[i][j] + mat[i][j]

        def check_size(sz):
            for i in range(n - sz + 1):
                j = i + sz - 1
                # [i..j], use dp[i+1..j+1]
                tmp = [0] * m
                for k in range(m):
                    tmp[k] = dp[j + 1][k] - dp[i][k]

                for k in range(1, m):
                    tmp[k] += tmp[k - 1]

                for k in range(sz - 1, m):
                    # use [k-sz+1 .. k]
                    v = tmp[k - sz] if k - sz >= 0 else 0
                    if (tmp[k] - v) <= threshold:
                        return True
            return False

        s, e = 1, min(n, m)
        ans = 0
        while s <= e:
            mid = (s + e) // 2
            if check_size(mid):
                ans = mid
                s = mid + 1
            else:
                e = mid - 1
        return ans


cases = [
    ([[1, 1, 3, 2, 4, 3, 2], [1, 1, 3, 2, 4, 3, 2], [1, 1, 3, 2, 4, 3, 2]], 4, 2),
    ([[1, 1, 1, 1], [1, 0, 0, 0], [1, 0, 0, 0], [1, 0, 0, 0]], 6, 3),
    ([[18, 70], [61, 1], [25, 85], [14, 40], [11, 96], [97, 96], [63, 45]], 40184, 2),
]

import aatest_helper

aatest_helper.run_test_cases(Solution().maxSideLength, cases)
