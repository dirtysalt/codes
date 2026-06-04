#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

def solve(n, m, values):
    matrix = [[0] * m for _ in range(n)]
    for idx, v in enumerate(values):
        matrix[idx // m][idx % m] = v

    transpose = False
    if n < m:
        matrix = list(zip(*matrix))
        n, m = m, n
        transpose = True

    # O(n^2 * m). so if n << m,
    # transpose matrix

    neg_inf = -(1 << 30)
    ans = neg_inf
    ans_position = None

    for i in range(n):
        temp = [0] * m
        for j in range(i, n):
            for k in range(m):
                temp[k] += matrix[j][k]

            # Kadane Algorithm.
            max_val, f, t = neg_inf, -1, -1
            idx, value = 0, 0
            for k in range(m):
                value += temp[k]
                if value < 0:
                    idx = k + 1
                    value = 0
                elif value > max_val:
                    max_val = value
                    f, t = idx, k

            # special case. all are negative.
            if max_val == neg_inf:
                for k in range(m):
                    if temp[k] > max_val:
                        max_val = temp[k]
                        f, t = k, k

            if max_val > ans:
                ans = max_val
                ans_position = [i, j, f, t]

    if transpose:
        ans_position = ans_position[-2:] + ans_position[:2]
    # print(ans_position)
    return ans


t = int(input())
for _ in range(t):
    n, m = [int(x) for x in input().split()]
    values = [int(x) for x in input().split()]
    print(solve(n, m, values))
