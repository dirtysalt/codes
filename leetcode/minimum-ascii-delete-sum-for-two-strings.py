#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        n, m = len(s1), len(s2)
        dp = []
        for i in range(n + 1):
            dp.append([-1] * (m + 1))

        dp[0][0] = 0
        v = 0
        for i in range(1, n + 1):
            v += ord(s1[i - 1])
            dp[i][0] = v
        v = 0
        for i in range(1, m + 1):
            v += ord(s2[i - 1])
            dp[0][i] = v

        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if s1[i - 1] == s2[j - 1]:
                    v = dp[i - 1][j - 1]
                else:
                    v = min(dp[i - 1][j] + ord(s1[i - 1]),
                            dp[i][j - 1] + ord(s2[j - 1]))
                dp[i][j] = v

        return dp[n][m]


def test():
    cases = [
        ("sea", "eat", 231),
        ("delete", "leet", 403),
    ]
    sol = Solution()
    ok = True
    for c in cases:
        (s1, s2, exp) = c
        res = sol.minimumDeleteSum(s1, s2)
        if res != exp:
            print('case failed. {}, out = {}'.format(c, res))
            ok = False
    if ok:
        print('cases passed!!!')


if __name__ == '__main__':
    test()
