#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def getProbability(self, balls: List[int]) -> float:
        n = len(balls)
        N = sum(balls) // 2

        C = [[0] * 10 for _ in range(10)]
        for i in range(10):
            C[i][0] = 1
            for j in range(1, i + 1):
                C[i][j] = C[i - 1][j] + C[i - 1][j - 1]

        fact = [1] * 10
        for i in range(1, 10):
            fact[i] *= fact[i - 1] * i

        tt, ok = 0, 0

        def search(i, k, diff, value):
            nonlocal tt, ok
            if i == n:
                if k != N:
                    return

                tt += value
                if diff == 0:
                    ok += value
                return

            if k + sum(balls[i:]) < N:
                return

            for c in range(0, balls[i] + 1):
                if (k + c) > N:
                    break
                v = value * C[balls[i]][c]
                df = diff
                if c == 0:
                    df += 1
                elif c == balls[i]:
                    df -= 1
                search(i + 1, k + c, df, v)

        search(0, 0, 0, 1)
        ans = round(ok / tt, 5)
        return ans


cases = [
    ([1, 1], 1.00000),
    ([2, 1, 1], 0.66667),
    ([6, 6, 6, 6, 6, 6], 0.90327),
    ([6, 6, 6, 6, 6, 6, 6, 6], 0.85571),
    ([1, 2, 1, 2], 0.60000),
    ([3, 2, 1], 0.30000)
]

import aatest_helper

aatest_helper.run_test_cases(Solution().getProbability, cases)
