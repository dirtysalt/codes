#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def distinctPrimeFactors(self, nums: List[int]) -> int:
        N = 1000
        P = [0] * (N + 1)
        for i in range(2, N + 1):
            if P[i] == 1: continue
            for j in range(2, N + 1):
                if i * j > N: break
                P[i * j] = 1
        PS = []
        for i in range(2, N + 1):
            if P[i] == 0: PS.append(i)

        ps = set()
        for x in nums:
            for p in PS:
                if x % p == 0:
                    while x % p == 0:
                        x = x // p
                    ps.add(p)
                    if x == 1: break
            if x != 1: ps.add(x)
        return len(ps)


if __name__ == '__main__':
    pass
