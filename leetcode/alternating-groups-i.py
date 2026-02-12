#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def numberOfAlternatingGroups(self, colors: List[int]) -> int:
        n = len(colors)
        ans = 0
        for i in range(n):
            a, b = i + 1, i + 2
            a, b = a % n, b % n
            if colors[i] == 1 - colors[a] == colors[b]:
                ans += 1
        return ans


if __name__ == '__main__':
    pass
