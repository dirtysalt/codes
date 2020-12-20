#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def allCellsDistOrder(self, R: int, C: int, r0: int, c0: int) -> List[List[int]]:
        ps = [(x, y) for x in range(R) for y in range(C)]
        ps.sort(key=lambda p: abs(p[0] - r0) + abs(p[1] - c0))
        return ps
