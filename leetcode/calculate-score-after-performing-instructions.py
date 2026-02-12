#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def calculateScore(self, instructions: List[str], values: List[int]) -> int:
        visit = set()
        ans = 0
        i = 0
        while i not in visit and 0 <= i < len(instructions):
            v = instructions[i]
            visit.add(i)
            if v == "add":
                ans += values[i]
                i += 1
            else:
                i += values[i]
        return ans


if __name__ == '__main__':
    pass
