#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from sys import stdin


def run(n, m, x, y, board):
    ans = 0
    inf = 1 << 30
    dp = [inf] * (m + 1)
    dp[0] = 0
    for i in range(m):
        if (i + 1) <= m:
            dp[i + 1] = min(dp[i + 1], dp[i] + x)
        if (i + 2) <= m:
            dp[i + 2] = min(dp[i + 2], dp[i] + y)

    for i in range(n):
        j = 0
        while j < m:
            if board[i][j] == '.':
                sz = 0
                while j < m and board[i][j] == '.':
                    j += 1
                    sz += 1
                ans += dp[sz]
            else:
                j += 1
    return ans


def main():
    t = int(stdin.readline())
    for _ in range(t):
        n, m, x, y = [int(x) for x in stdin.readline().split()]
        board = []
        for _ in range(n):
            board.append(stdin.readline().strip())
        ans = run(n, m, x, y, board)
        print(ans)


if __name__ == '__main__':
    import os

    if os.path.exists('tmp.in'):
        stdin = open('tmp.in')
    main()
