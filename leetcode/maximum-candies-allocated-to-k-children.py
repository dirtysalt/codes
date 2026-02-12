#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:

        def test(t):
            c = 0
            for x in candies:
                c += x // t
            return c >= k

        s, e = 1, max(candies)
        while s <= e:
            m = (s + e) // 2
            if test(m):
                s = m + 1
            else:
                e = m - 1
        return e


if __name__ == '__main__':
    pass
