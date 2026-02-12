#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        n = len(colors)
        ans = 0
        for i in range(n):
            for j in reversed(range(i + 1, n)):
                if colors[i] != colors[j]:
                    ans = max(ans, j - i)
        return ans


if __name__ == '__main__':
    pass
