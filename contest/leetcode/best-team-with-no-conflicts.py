#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        n = len(scores)
        xs = list(zip(ages, scores))
        xs.append((0, 0))
        xs.sort()

        dp = [0] * (n + 1)
        dp[0] = 0
        for i in range(n + 1):
            for j in range(i + 1, n + 1):
                if xs[j][0] == xs[i][0] or xs[j][1] >= xs[i][1]:
                    dp[j] = max(dp[j], dp[i] + xs[j][1])
        ans = max(dp)
        return ans


cases = [
    ([1, 3, 5, 10, 15], [1, 2, 3, 4, 5], 34),
    ([4, 5, 6, 5], [2, 1, 2, 1], 16),
    ([1, 2, 3, 5], [8, 9, 10, 1], 6),
    ([1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [811, 364, 124, 873, 790, 656, 581, 446, 885, 134], 10),
]

import aatest_helper

aatest_helper.run_test_cases(Solution().bestTeamScore, cases)
