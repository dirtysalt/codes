#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt


def solve(exp):
    n = len(exp)
    dp = []
    for i in range(n):
        dp.append([(0, 0)] * n)

    for i in range(0, n, 2):
        if exp[i] == 'T':
            dp[i][i] = (1, 0)
        else:
            dp[i][i] = (0, 1)

    MOD = 1003
    for k in range(3, n + 1, 2):
        for i in range(0, n - k + 1, 2):
            j = i + k
            # exp[i..j]
            res_true, res_false = 0, 0
            for op_idx in range(i + 1, j - 1, 2):
                va = dp[i][op_idx - 1]
                vb = dp[op_idx + 1][j - 1]
                op = exp[op_idx]
                if op == '&':
                    res_true += va[0] * vb[0]
                    res_false += (va[1] * vb[0] + va[0] * vb[1] + va[1] * vb[1])
                elif op == '|':
                    res_true += (va[0] * vb[0] + va[0] * vb[1] + va[1] * vb[0])
                    res_false += (va[1] * vb[1])
                elif op == '^':
                    res_true += (va[0] * vb[1] + va[1] * vb[0])
                    res_false += (va[1] * vb[1] + va[0] * vb[0])
                else:
                    assert op in '&|^'
            res_true %= MOD
            res_false %= MOD
            dp[i][j - 1] = (res_true, res_false)
    return dp[0][n - 1][0]


t = int(input())
for _ in range(t):
    n = int(input())
    exp = input().rstrip()
    print(solve(exp))
