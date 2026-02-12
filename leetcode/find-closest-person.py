#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt


class Solution:
    def findClosest(self, x: int, y: int, z: int) -> int:
        a, b = abs(x - z), abs(y - z)
        if a < b:
            return 1
        elif a > b:
            return 2
        return 0


if __name__ == '__main__':
    pass
