#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def smallestValue(self, n: int) -> int:
        PS = [0] * (n + 1)
        for i in range(2, n + 1):
            if PS[i] == 1: continue
            for j in range(2, n + 1):
                if i * j > n: break
                PS[i * j] = 1

        PS2 = []
        for i in range(2, n + 1):
            if PS[i] == 0:
                PS2.append(i)

        def findNext(x):
            if PS[x] == 0: return x
            ans = 0
            for y in PS2:
                if x % y == 0:
                    while x % y == 0:
                        ans += y
                        x = x // y
            if x != 1: ans += x
            return ans

        while True:
            n2 = findNext(n)
            if n == n2: break
            n = n2
        return n


if __name__ == '__main__':
    pass
