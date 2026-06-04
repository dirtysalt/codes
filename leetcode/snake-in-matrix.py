#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def finalPositionOfSnake(self, n: int, commands: List[str]) -> int:
        d = {'UP': (-1, 0), 'DOWN': (1, 0), 'LEFT': (0, -1), 'RIGHT': (0, 1)}
        i, j = 0, 0
        for c in commands:
            x, y = d[c]
            i, j = i + x, j + y
        return i * n + j


if __name__ == '__main__':
    pass
