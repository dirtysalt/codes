#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        n = len(questions)
        dp = [0] * (n + 1)

        for i in range(n):
            dp[i + 1] = max(dp[i + 1], dp[i])

            (p, k) = questions[i]
            j = min(n, i + k + 1)
            dp[j] = max(dp[j], dp[i] + p)

        ans = max(dp)
        return ans


if __name__ == '__main__':
    pass
