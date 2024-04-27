#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt


class SolutionCache:
    def numberOfStableArrays(self, zero: int, one: int, limit: int) -> int:
        MOD = 10 ** 9 + 7
        import numpy as np

        dp = np.zeros((zero + 1, one + 1, 2, limit + 1), np.int64)
        dp[:, :, :, :] = -1

        def dfs(a, b, c, d):
            if d > limit: return 0
            if a == zero and b == one:
                return 1
            if dp[a][b][c][d] != -1:
                return dp[a][b][c][d]

            r = 0
            if (a + 1) <= zero:
                r += dfs(a + 1, b, 0, (d + 1) if c == 0 else 1)
            if (b + 1) <= one:
                r += dfs(a, b + 1, 1, (d + 1) if c == 1 else 1)
            dp[a][b][c][d] = r % MOD
            return r % MOD

        ans = dfs(0, 0, -1, 0)
        return int(ans)


class SolutionNP:
    def numberOfStableArrays(self, zero: int, one: int, limit: int) -> int:
        import numpy as np
        dp = np.zeros((zero + 1, one + 1, limit + 1, 2), np.int64)
        dp[1][0][1][0] = 1
        dp[0][1][1][1] = 1

        MOD = 10 ** 9 + 7

        def update(i, j, k, c, num):
            dp[i][j][k][c] = (dp[i][j][k][c] + num) % MOD

        for i in range(zero + 1):
            for j in range(one + 1):
                for k in range(1, limit + 1):
                    for c in (0, 1):
                        num = dp[i][j][k][c]

                        if (i + 1) <= zero:
                            if c == 0 and k < limit:
                                update(i + 1, j, k + 1, 0, num)
                            elif c == 1:
                                update(i + 1, j, 1, 0, num)

                        if (j + 1) <= one:
                            if c == 1 and k < limit:
                                update(i, j + 1, k + 1, 1, num)
                            elif c == 0:
                                update(i, j + 1, 1, 1, num)

        ans = np.sum(dp[zero][one]) % MOD
        return int(ans)


class Solution:
    def numberOfStableArrays(self, zero: int, one: int, limit: int) -> int:
        import numpy as np
        dp = np.zeros((zero + 1, one + 1, 2), np.int64).tolist()
        MOD = 10 ** 9 + 7

        # dp[x][y][z] -> x 0, y 1, endswith z[0/1]

        # place k zeros in a group.
        # dp[x][y][0] = sum (dp[x-k][y][1]) k = [1 .. min(x, limit)]
        #    dp[x-k][y][1] + dp[x-(k+1)[y][1] + .. dp[x-1][y][1]
        #    acc[x][y][1] - acc[x-k][y][1]

        for k in range(1, min(zero, limit) + 1):
            dp[k][0][0] = 1
        for k in range(1, min(one, limit) + 1):
            dp[0][k][1] = 1

        for x in range(zero + 1):
            for y in range(one + 1):
                # try z = 0
                if True:
                    k = min(x, limit)
                    cost = 0
                    for z in range(1, k + 1):
                        cost += dp[x - z][y][1]
                    dp[x][y][0] = (dp[x][y][0] + cost)

                # try z = 1
                if True:
                    k = min(y, limit)
                    cost = 0
                    for z in range(1, k + 1):
                        cost += dp[x][y - z][0]
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
