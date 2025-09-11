#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def interchangeableRectangles(self, rectangles: List[List[int]]) -> int:
        from collections import Counter
        ans = 0
        cnt = Counter()

        def gcd(x, y):
            while y != 0:
                x, y = y, x % y
            return x

        for x, y in rectangles:
            g = gcd(x, y)
            x = x // g
            y = y // g
            z = (x, y)
            p = cnt[z]
            ans += p
            cnt[z] = p + 1

        return ans


if __name__ == '__main__':
    pass
