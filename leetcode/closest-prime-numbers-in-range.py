#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        N = max(left, right)
        P = [0] * (N + 1)
        for i in range(2, N + 1):
            if P[i] == 1: continue
            for j in range(2, N + 1):
                if i * j > N: break
                P[i * j] = 1

        PS = []
        for i in range(2, N + 1):
            if P[i] == 0 and i >= left and i <= right:
                PS.append(i)

        if len(PS) < 2: return [-1, -1]
        idx = 1
        for i in range(2, len(PS)):
            if (PS[i] - PS[i - 1]) < (PS[idx] - PS[idx - 1]):
                idx = i
        return [PS[idx - 1], PS[idx]]


if __name__ == '__main__':
    pass
