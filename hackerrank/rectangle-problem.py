#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

# https://www.hackerrank.com/contests/iiti-league-contest-1/challenges/rectangle-problem

def solve(a, b, x, y):
    if 0 < x < a and 0 < y < b:
        return 0
    elif 0 <= x <= a and 0 <= y <= b:
        return 1
    return 2


t = int(input())
for _ in range(t):
    a, b = [int(x) for x in input().rstrip().split()]
    x, y = [int(x) for x in input().rstrip().split()]
    print((solve(a, b, x, y)))
