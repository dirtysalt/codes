#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        dp = {}
        sz = len(words[0])
        target = [ord(x) - ord('a') for x in target]
        MOD = 10 ** 9 + 7

        indices = [[] for _ in range(26)]
        for w in words:
            for i in range(len(w)):
                c = ord(w[i]) - ord('a')
                indices[c].append(i)
        for x in indices:
            x.sort()

        # print(indices)

        def searchPositions(c, k):
            import bisect
            i = bisect.bisect_left(indices[c], k)
            while i < len(indices[c]):
                yield indices[c][i]
                i += 1

        def fun(i, k):
            if i == len(target):
                return 1

            key = (i, k)
            if key in dp: return dp[key]
            ans = 0
            # search possible positions >= k+1.
            for p in searchPositions(target[i], k + 1):
                if (sz - (p + 1)) < (len(target) - (i + 1)):
                    break
                ans += fun(i + 1, p)
            dp[key] = ans
            return ans

        ans = fun(0, -1)
        return ans % MOD


# dp[i][k] = if c[k] == target[i], then dp[i-1][k-1] + dp[i-1][k-2] + ...
# dp[i][k+1] = if c[k+1] == target[i], then dp[i-1][k] + dp[i-1][k-1] + dp[i-1][k-2] + ...

class Solution2:
    def numWays(self, words: List[str], target: str) -> int:
        sz = len(words[0])
        n = len(target)
        MOD = 10 ** 9 + 7

        target = [ord(x) - ord('a') for x in target]
        from collections import Counter
        indices = [Counter() for _ in range(26)]
        for w in words:
            for i in range(len(w)):
                c = ord(w[i]) - ord('a')
                indices[c][i] += 1

        dp = [[0] * (sz + 1) for _ in range(n + 1)]
        dp[0][0] = 1

        for i in range(n):
            acc = 0
            for k in range(sz):
                acc += dp[i][k]
                occ = indices[target[i]][k]
                dp[i + 1][k + 1] = acc * occ

        ans = sum(dp[n])
        return ans % MOD


cases = [
    (["acca", "bbbb", "caca"], "aba", 6),
    (["abba", "baab"], "bab", 4),
    (["abcd"], "abcd", 1),
    (["abab", "baba", "abba", "baab"], "abba", 16),
]

import aatest_helper

aatest_helper.run_test_cases(Solution().numWays, cases)
aatest_helper.run_test_cases(Solution2().numWays, cases)
