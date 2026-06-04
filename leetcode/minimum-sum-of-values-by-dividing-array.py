#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def minimumValueSum(self, nums: List[int], andValues: List[int]) -> int:
        n, m = len(nums), len(andValues)

        BITS = 20
        acc = [[0] * BITS for _ in range(n + 1)]
        for i in range(n):
            x = nums[i]
            for b in range(BITS):
                if x & (1 << b):
                    acc[i + 1][b] += 1
            for b in range(BITS):
                acc[i + 1][b] += acc[i][b]

        def query(s, e):
            v = 0
            for b in range(BITS):
                c = acc[e + 1][b] - acc[s][b]
                if c == (e - s + 1):
                    v = v | (1 << b)
            return v

        import functools
        @functools.cache
        def find_first(start, index):
            value = andValues[index]
            s, e = start, n - 1
            while s <= e:
                m = (s + e) // 2
                v = query(start, m)
                if (v | value) == value:
                    e = m - 1
                else:
                    s = m + 1
            if s == n: return -1
            v = query(start, s)
            if v != value: return -1
            return s

        INF = 1 << 30
        dp = [[INF] * m for _ in range(n)]
        p = find_first(0, 0)
        if p == -1: return -1
        dp[p][0] = nums[p]

        for i in range(n):
            for j in range(m):
                if dp[i][j] == INF or (i + 1) == n: continue

                if (andValues[j] & nums[i + 1]) == andValues[j]:
                    # dp[i+1][j] <- dp[i][j] - nums[i] + nums[i+1]
                    dp[i + 1][j] = min(dp[i + 1][j], dp[i][j] - nums[i] + nums[i + 1])

                if (j + 1) < m:
                    # or we can create a neww group.
                    p = find_first(i + 1, j + 1)
                    if p != -1:
                        dp[p][j + 1] = min(dp[p][j + 1], dp[i][j] + nums[p])

        ans = dp[n - 1][m - 1]
        return ans if ans != INF else -1


class Solution:
    def minimumValueSum(self, nums: List[int], andValues: List[int]) -> int:
        n, m = len(nums), len(andValues)
        INF = 1 << 30

        import functools
        @functools.cache
        def dfs(i, j, andv):
            if n - i < m - j: return INF
            if j == m:
                return 0 if i == n else INF

            andv &= nums[i]
            if andv < andValues[j]:
                return INF

            r = dfs(i + 1, j, andv)
            if andv == andValues[j]:
                r2 = dfs(i + 1, j + 1, -1) + nums[i]
                r = min(r, r2)
            return r

        ans = dfs(0, 0, -1)
        return ans if ans != INF else -1


true, false, null = True, False, None
import aatest_helper

cases = [
    aatest_helper.OrderedDict(nums=[1, 4, 3, 3, 2], andValues=[0, 3, 3, 2], res=12),
    aatest_helper.OrderedDict(nums=[2, 3, 5, 7, 7, 7, 5], andValues=[0, 7, 5], res=17),
    aatest_helper.OrderedDict(nums=[1, 2, 3, 4], andValues=[2], res=-1),
    ([1, 3, 2, 4, 7, 5, 3], [0, 5, 3], 12),
    ([1, 3, 2, 4, 7, 5], [0, 5], 9),
    ([1, 3, 2, 4], [0], 4)
]

aatest_helper.run_test_cases(Solution().minimumValueSum, cases)

if __name__ == '__main__':
    pass
