#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def maxRemovals(self, source: str, pattern: str, targetIndices: List[int]) -> int:
        # dp[i][j] = remove how many chars.
        #      dp[i+1][j] + (i in target)
        # .     dp[i+1][j+1] if (s[i] = p[j])

        n, m = len(source), len(pattern)
        target = set(targetIndices)
        dp = [[-1] * (m + 1) for _ in range(n + 1)]
        dp[0][0] = 0
        for i in range(n):
            for j in range(m + 1):
                if dp[i][j] == -1: continue
                if j == m:
                    dp[i + 1][j] = max(dp[i + 1][j], dp[i][j] + (i in target))
                else:
                    # do match.
                    if source[i] == pattern[j]:
                        dp[i + 1][j + 1] = max(dp[i + 1][j + 1], dp[i][j])
                    dp[i + 1][j] = max(dp[i + 1][j], dp[i][j] + (i in target))
        return dp[n][m]


true, false, null = True, False, None
import aatest_helper

cases = [
    aatest_helper.OrderedDict(source="abbaa", pattern="aba", targetIndices=[0, 1, 2], res=1),
    aatest_helper.OrderedDict(source="bcda", pattern="d", targetIndices=[0, 3], res=2),
    aatest_helper.OrderedDict(source="dda", pattern="dda", targetIndices=[0, 1, 2], res=0),
    aatest_helper.OrderedDict(source="yeyeykyded", pattern="yeyyd", targetIndices=[0, 2, 3, 4], res=2),
]

aatest_helper.run_test_cases(Solution().maxRemovals, cases)

if __name__ == '__main__':
    pass
