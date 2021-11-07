#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:

        def ok(m):
            res = 0
            for q in quantities:
                res += (q + m - 1) // m

            return res <= n

        s, e = 1, max(quantities)
        while s <= e:
            m = (s + e) // 2
            if ok(m):
                e = m - 1
            else:
                s = m + 1

        return s


if __name__ == '__main__':
    pass
