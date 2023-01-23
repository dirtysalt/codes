#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt


# def solve(xs):
#     xs.sort()
#     n = len(xs)
#     max_value = n * xs[-1]
#     dp = [0] * (max_value + 1)
#     dp[0] = 1
#     for x in xs:
#         for i in range(max_value - x, -1, -1):
#             if not dp[i]:
#                 continue
#             v = i + x
#             dp[v] = 1
#     for i in range(0, max_value + 1):
#         if not dp[i]:
#             return i
#     return max_value + 1

def solve(xs):
    xs.sort()
    res = 1
    for x in xs:
        if x > res:
            break
        res += x
    return res


t = int(input())
for _ in range(t):
    n = int(input())
    xs = [int(x) for x in input().rstrip().split()]
    print(solve(xs))
