#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt


class Solution:
    def numberOfStableArrays(self, zero: int, one: int, limit: int) -> int:
        dp = [[[0] * 2 for _ in range(one + 1)] for _ in range(zero + 1)]
        MOD = 10 ** 9 + 7

        # dp[x][y][z] -> x 0, y 1, endswith z[0/1]
        # place k zeros in a group.
        # dp[x][y][0] = sum (dp[x-k][y][1]) k = [1 .. min(x, limit)]

        for k in range(1, min(zero, limit) + 1):
            dp[k][0][0] = 1
        for k in range(1, min(one, limit) + 1):
            dp[0][k][1] = 1

        acc = [0] * (one + 1)
        for x in range(zero + 1):
            # try z = 0
            k = min(x, limit)
            for y in range(one + 1):
                acc[y] += dp[x - 1][y][1] if x >= 1 else 0
                if x > k:
                    acc[y] -= dp[x - k - 1][y][1]
                cost = acc[y]
                dp[x][y][0] = (dp[x][y][0] + cost)

            # try z = 1
            cost = 0
            for y in range(one + 1):
                cost += dp[x][y - 1][0] if (y >= 1) else 0
                k = min(y, limit)
                if y > k:
                    cost -= dp[x][y - k - 1][0]
                dp[x][y][1] = (dp[x][y][1] + cost)
        ans = dp[zero][one][0] + dp[zero][one][1]
        ans = ans % MOD

        return ans


true, false, null = True, False, None
import aatest_helper

cases = [
    (1, 1, 2, 2),
    (1, 2, 1, 1),
    (3, 3, 2, 14),
    (55, 58, 32, 941010913),
    (37, 53, 90, 446823581)
]

aatest_helper.run_test_cases(Solution().numberOfStableArrays, cases)

if __name__ == '__main__':
    pass
