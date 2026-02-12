#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def largestPalindrome(self, n: int, K: int) -> str:

        REM = [0] * n
        REM[0] = 1
        for i in range(1, n):
            REM[i] = (REM[i - 1] * 10) % K

        import functools
        @functools.cache
        def dfs(i, j, rem):
            if i < j: return "" if rem == 0 else None

            end = 0
            if j == 0: end = 1
            if i == j:
                for k in range(9, end - 1, -1):
                    if (k * REM[i]) % K == rem:
                        return str(k)
                return None

            for k in range(9, end - 1, -1):
                # k * (10 << i)
                # k * (10 << j)
                a = (k * REM[i]) % K
                b = (k * REM[j]) % K
                exp = (rem + 2 * K - a - b) % K
                res = dfs(i - 1, j + 1, exp)
                if res is None: continue
                return str(k) + res + str(k)

            return None

        ans = dfs(n - 1, 0, 0)
        dfs.cache_clear()
        return ans


class Solution:
    def largestPalindrome(self, n: int, K: int) -> str:
        REM = [0] * n
        REM[0] = 1
        for i in range(1, n):
            REM[i] = (REM[i - 1] * 10) % K

        # dp[i][rem] = k
        dp = [[-1] * 10 for _ in range((n + 1) // 2 + 1)]
        if n % 2 == 1:
            mid = n // 2
            for k in range(10):
                rem = (REM[mid] * k) % K
                dp[mid][rem] = k
        else:
            mid = n // 2 - 1
            for k in range(10):
                rem = (REM[mid] + REM[mid + 1]) * k % K
                dp[mid][rem] = k

        for j in reversed(range(mid)):
            for rem in range(10):
                start = 0 if j > 0 else 1
                for k in reversed(range(start, 10)):
                    a = (REM[j] + REM[n - 1 - j]) * k % K
                    exp = (rem + K - a) % K
                    if dp[j + 1][exp] != -1:
                        dp[j][rem] = k
                        break

        ans = []
        rem = 0
        for j in range(mid + 1):
            k = dp[j][rem]
            ans.append(str(k))
            a = (REM[j] + REM[n - 1 - j]) * k % K
            exp = (rem + K - a) % K
            rem = exp

        if n % 2 == 1:
            r = ans[:-1]
            res = r + list(ans[-1]) + r[::-1]
        else:
            res = ans + ans[::-1]
        return ''.join(res)


true, false, null = True, False, None
import aatest_helper

cases = [
    (3, 5, "595"),
    (1, 4, "8"),
    (5, 6, "89898"),
    (10000, 4, aatest_helper.ANYTHING)
]

aatest_helper.run_test_cases(Solution().largestPalindrome, cases)

if __name__ == '__main__':
    pass
