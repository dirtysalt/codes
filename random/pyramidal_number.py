#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

def pyramidal_number(n, k):
    dp = [[0] * (k + 1) for _ in range(n + 1)]
    dp[0][0] = 1
    for i in range(1, n + 1):
        j = 2
        while True:
            x = (j ** 3 - j) // 6
            j += 1
            if x > i:
                break
            if x == i:
                dp[i][0] = 1
            for k2 in range(1, k + 1):
                dp[i][k2] = dp[i][k2] or dp[i - x][k2 - 1]
    ans = 0
    for i in range(1, n + 1):
        ok = False
        for k2 in range(1, k + 1):
            if dp[i][k2] == 1:
                ok = True
                break
        if ok:
            ans += 1
    return ans


if __name__ == '__main__':
    ans = pyramidal_number(10 ** 6, k=5)
    print(ans)
