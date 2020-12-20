#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def queensAttacktheKing(self, queens: List[List[int]], king: List[int]) -> List[List[int]]:
        ans = []
        qs = set()
        for x, y in queens:
            qs.add((x, y))

        for dx in range(-1, 2):
            for dy in range(-1, 2):
                x, y = king
                if dx == 0 and dy == 0: continue
                while 0 <= x < 8 and 0 <= y < 8:
                    if (x, y) in qs:
                        ans.append((x, y))
                        break
                    x += dx
                    y += dy

        return ans
