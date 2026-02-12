#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def minimumCost(self, m: int, n: int, horizontalCut: List[int], verticalCut: List[int]) -> int:
        ops = [(x, 0) for x in horizontalCut]
        ops += [(x, 1) for x in verticalCut]
        ops.sort(key=lambda x: -x[0])
        ans, h, v = 0, 1, 1

        for x, ty in ops:
            if ty == 0:
                ans += x * v
                h += 1
            else:
                ans += x * h
                v += 1
        return ans


if __name__ == '__main__':
    pass
