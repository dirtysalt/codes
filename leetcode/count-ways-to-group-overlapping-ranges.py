#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def countWays(self, ranges: List[List[int]]) -> int:
        ev = []
        for s, e in ranges:
            ev.append((s, 0))
            ev.append((e + 1, -1))
        ev.sort()

        counts = []
        cnt, dep = 0, 0
        for x, y in ev:
            if y == -1:
                dep -= 1
                if dep == 0:
                    counts.append(cnt)
                    cnt = 0
            else:
                dep += 1
                cnt += 1

        def pow(a, b, MOD):
            ans = 1
            while b:
                if b & 0x1:
                    ans = (ans * a) % MOD
                b = b >> 1
                a = (a * a) % MOD
            return ans

        MOD = 10 ** 9 + 7
        ans = pow(2, len(counts), MOD)
        return ans


if __name__ == '__main__':
    pass
