#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def makeSubKSumEqual(self, arr: List[int], k: int) -> int:
        def group(xs):
            xs.sort()
            tt = sum([x - xs[0] for x in xs])
            ans = tt
            l, r = 1, len(xs) - 1
            for i in range(1, len(xs)):
                d = xs[i] - xs[i - 1]
                tt += l * d - r * d
                l, r = l + 1, r - 1
                ans = min(ans, tt)
            return ans

        n = len(arr)
        g = [-1] * n
        ans = 0
        for i in range(n):
            if g[i] != -1: continue
            xs = []
            while g[i] == -1:
                g[i] = 0
                xs.append(arr[i])
                i = (i + k) % n
            r = group(xs)
            print(i, r)
            ans += r
        return ans


if __name__ == '__main__':
    pass
