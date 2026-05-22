#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def minimumPartition(self, s: str, k: int) -> int:

        n = len(s)
        INF = 1 << 30
        dp = [INF] * (n + 1)
        dp[0] = 0

        for i in range(n):
            j = i
            r = 0
            while j < n:
                r = r * 10 + ord(s[j]) - ord('0')
                if r > k: break
                j += 1
                dp[j] = min(dp[j], dp[i] + 1)
        ans = dp[n]
        if ans == INF:
            ans = -1
        return ans


if __name__ == '__main__':
    pass
