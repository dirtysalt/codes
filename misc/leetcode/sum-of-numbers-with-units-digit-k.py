#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def minimumNumbers(self, num: int, k: int) -> int:
        inf = 1 << 30
        dp = [inf] * (1 + num)
        dp[0] = 0

        for i in range(num):
            x = k
            if k == 0: x = 10
            while i + x <= num:
                dp[i + x] = min(dp[i + x], 1 + dp[i])
                x += 10

        ans = dp[num]
        if ans == inf:
            ans = -1
        return ans


if __name__ == '__main__':
    pass
