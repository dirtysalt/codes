#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt
from sys import stdin


def solve(graph, n):
    inf = 1 << 30
    neg_inf = -inf

    # for i in range(n):
    #     print(graph[i])

    dp = [[[neg_inf for _ in range(n)] for _ in range(n)] for _ in range(2)]
    now = 0
    dp[now][0][0] = graph[0][0]

    def get_dp(k, i, j):
        if i < 0 or j < 0:
            return neg_inf
        return dp[k][i][j]

    for step in range(1, 2 * n - 1):
        for i in range(n):
            for j in range(n):
                # if 0 <= (step - i) < n and 0 <= (step - j) < n:
                if i > step or j > step: continue
                if (i + n) <= step or (j + n) <= step: continue
                res = max(get_dp(now, i - 1, j), get_dp(now, i, j - 1),
                          get_dp(now, i - 1, j - 1), get_dp(now, i, j))
                res += graph[i][step - i]
                if i != j:
                    res += graph[j][step - j]
                dp[1 - now][i][j] = res
        now = 1 - now

    return dp[now][n - 1][n - 1]


# stdin = open('input.in')
n = int(stdin.readline())
graph = [[0 for _ in range(n)] for _ in range(n)]
while True:
    a, b, c = [int(x) for x in stdin.readline().split()]
    if not (a and b and c):
        break
    graph[a - 1][b - 1] = c

ans = solve(graph, n)
print(ans)
