#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def getMaxGridHappiness(self, m: int, n: int, introvertsCount: int, extrovertsCount: int) -> int:
        dp = {}

        def updatePlace(r, c, st, p):
            score = 0
            if p == 1:
                score += 120
                delta = -30
            elif p == 2:
                score += 40
                delta = 20
            assert p != 3

            up = st & 0x3
            assert up != 3
            if up != 0:
                score += delta
            if up == 1:
                score -= 30
            elif up == 2:
                score += 20

            if c != 0:
                left = (st >> (2 * n - 2)) & 0x3
                assert left != 3
                if left != 0:
                    score += delta
                if left == 1:
                    score -= 30
                elif left == 2:
                    score += 20
            return score

        key = (-1, 0, 0, 0)
        dp[key] = 0

        def updateDP(idx, st, j, k, score):
            key = (idx, st, j, k)
            # print(key, score)
            if key not in dp:
                dp[key] = score
            else:
                dp[key] = max(score, dp[key])

        for idx in range(m * n):
            for st in range(1 << (2 * n)):
                for j in range(introvertsCount + 1):
                    for k in range(extrovertsCount + 1):
                        key = (idx - 1, st, j, k)
                        if key not in dp: continue
                        score = dp[key]
                        r, c = idx // n, idx % n

                        # if a introvert.
                        if j < introvertsCount:
                            res = updatePlace(r, c, st, 1)
                            st2 = 1 << (2 * n - 2) | (st >> 2)
                            updateDP(idx, st2, j + 1, k, res + score)

                        if k < extrovertsCount:
                            res = updatePlace(r, c, st, 2)
                            st2 = 1 << (2 * n - 1) | (st >> 2)
                            updateDP(idx, st2, j, k + 1, res + score)

                        updateDP(idx, st >> 2, j, k, score)

        # print(dp)
        ans = max(dp.values())
        return ans


cases = [
    (2, 3, 1, 2, 240),
    (3, 1, 2, 1, 260),
    (1, 3, 2, 0, 240),
    (5, 5, 6, 6, 1240)
]

import aatest_helper

aatest_helper.run_test_cases(Solution().getMaxGridHappiness, cases)
