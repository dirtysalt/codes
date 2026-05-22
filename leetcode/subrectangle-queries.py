#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class SubrectangleQueries:

    def __init__(self, rectangle: List[List[int]]):
        self.rect = rectangle
        self.ops = []

    def updateSubrectangle(self, row1: int, col1: int, row2: int, col2: int, newValue: int) -> None:
        self.ops.append((row1, col1, row2, col2, newValue))

    def getValue(self, row: int, col: int) -> int:
        ans = self.rect[row][col]
        for op in reversed(self.ops):
            r1, c1, r2, c2, v = op
            if r1 <= row <= r2 and c1 <= col <= c2:
                ans = v
                break
        return ans

# Your SubrectangleQueries object will be instantiated and called as such:
# obj = SubrectangleQueries(rectangle)
# obj.updateSubrectangle(row1,col1,row2,col2,newValue)
# param_2 = obj.getValue(row,col)
