#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def findWinningPlayer(self, skills: List[int], k: int) -> int:
        c, j = 0, 0
        for i in range(1, len(skills)):
            if skills[i] > skills[j]:
                c, j = 1, i
            else:
                c += 1
            if c == k: return j
        return j


if __name__ == '__main__':
    pass
