#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def countPairs(self, coordinates: List[List[int]], k: int) -> int:
        from collections import Counter
        cnt = Counter((tuple(x) for x in coordinates))

        ans = 0
        for x, y in coordinates:
            for kx in range(0, k + 1):
                ex = kx ^ x
                ey = (k - kx) ^ y
                ans += cnt[(ex, ey)]
                if (ex, ey) == (x, y):
                    ans -= 1
        return ans // 2


if __name__ == '__main__':
    pass
