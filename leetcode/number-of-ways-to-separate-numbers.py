#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt


class SolutionHash:
    def numberOfCombinations(self, num: str) -> int:
        if not num or num[0] == '0': return 0
        MOD = 10 ** 9 + 7
        n = len(num)

        dp = [[0] * n for _ in range(n)]
        hash = [[0] * n for _ in range(n)]

        for i in range(n):
            acc = 0
            for j in range(i, n):
                x = ord(num[j]) - ord('0')
                acc = acc * 11 + x
                acc = acc % MOD
                hash[i][j] = acc

        for i in range(n):
            dp[0][i] = 1

        for i in range(1, n):
            if num[i] == '0': continue
            for j in range(i, n):
                if (j - 1) >= i:
                    dp[i][j] += dp[i][j - 1]

                    # check some cases not counted before.
                    # num[p..i-1] and num[i..j-1]
                    p = 2 * i - j
                    if p >= 0 and num[p] != '0':
                        if hash[p][i - 1] != hash[i][j - 1] and num[p:i] > num[i:j]:
                            dp[i][j] += dp[p][i - 1]

                p = 2 * i - j
                # num[p-1..i-1] and num[i..j]
                if p >= 1 and num[p - 1] != '0':
                    if hash[p - 1][i - 1] == hash[i][j] or num[p - 1:i] <= num[i:j + 1]:
                        dp[i][j] += dp[p - 1][i - 1]

                dp[i][j] %= MOD

        ans = 0
        for i in range(n):
            # print(dp[i][n - 1])
            ans += dp[i][n - 1]
        ans = ans % MOD
        return ans


class Solution:
    def numberOfCombinations(self, num: str) -> int:
        if not num or num[0] == '0': return 0
        MOD = 10 ** 9 + 7
        n = len(num)

        dp = [[0] * n for _ in range(n)]
        lcp = [[0] * n for _ in range(n)]

        for i in reversed(range(n)):
            for j in reversed(range(n)):
                if num[i] == num[j]:
                    if (i + 1) < n and (j + 1) < n:
                        lcp[i][j] = lcp[i + 1][j + 1]
                    else:
                        lcp[i][j] = 0
                    lcp[i][j] += 1

        # print(lcp[4][3])

        for i in range(n):
            dp[0][i] = 1

        for i in range(1, n):
            if num[i] == '0': continue
            for j in range(i, n):
                if (j - 1) >= i:
                    dp[i][j] += dp[i][j - 1]

                    # check some cases not counted before.
                    # num[p..i-1] and num[i..j-1]
                    p = 2 * i - j
                    d = lcp[p][i]
                    if p >= 0 and num[p] != '0' and num[p + d:i] > num[i + d:j]:
                        dp[i][j] += dp[p][i - 1]

                p = 2 * i - j
                d = lcp[p - 1][i]
                # num[p-1..i-1] and num[i..j]
                if p >= 1 and num[p - 1] != '0' and num[p - 1 + d:i] <= num[i + d:j + 1]:
                    dp[i][j] += dp[p - 1][i - 1]

                dp[i][j] %= MOD

        ans = 0
        for i in range(n):
            # print(dp[i][n - 1])
            ans += dp[i][n - 1]
        ans = ans % MOD
        return ans


true, false, null = True, False, None
cases = [
    ("327", 2),
    ("094", 0),
    ("0", 0),
    ("9999999999999", 101),
    ("8412411824", 11),
    ('1' * 3500, 755568658)
]

import aatest_helper

aatest_helper.run_test_cases(Solution().numberOfCombinations, cases)

if __name__ == '__main__':
    pass
