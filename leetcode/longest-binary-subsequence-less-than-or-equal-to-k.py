#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def longestSubsequence(self, s: str, k: int) -> int:
        n = len(s)
        inf = 10 ** 9 + 1
        dp = [inf] * (n + 1)
        dp[0] = 0

        for i in range(n):
            x = ord(s[i]) - ord('0')
            for sz in reversed(range(n)):
                if dp[sz] == inf: continue
                v = dp[sz]
                nv = v * 2 + x
                dp[sz + 1] = min(dp[sz + 1], nv)

        for sz in reversed(range(n + 1)):
            if dp[sz] <= k:
                return sz
        return -1


if __name__ == '__main__':
    pass
