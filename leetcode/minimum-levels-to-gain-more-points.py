#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def minimumLevels(self, possible: List[int]) -> int:
        total = 0
        for x in possible:
            total += (-1 if x == 0 else 1)

        now = 0
        for idx, x in enumerate(possible[:-1]):
            d = (-1 if x == 0 else 1)
            now += d
            total -= d
            if now > total:
                return idx + 1
        return -1


if __name__ == '__main__':
    pass
