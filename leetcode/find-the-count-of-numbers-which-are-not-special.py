#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

def get_primes(N):
    P = [0] * N
    PS = []
    for x in range(2, N):
        if P[x] == 1: continue
        PS.append(x)
        for j in range(2, N):
            if x * j >= N: break
            P[x * j] = 1
    return PS


class Solution:
    def nonSpecialCount(self, l: int, r: int) -> int:
        N = 5 * (10 ** 4)
        PS = get_primes(N)
        ans = r - l + 1
        for x in PS:
            if x * x > r: break
            if x * x >= l: ans -= 1
        return ans


if __name__ == '__main__':
    pass
