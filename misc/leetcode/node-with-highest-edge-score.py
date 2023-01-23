#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def edgeScore(self, edges: List[int]) -> int:
        n = len(edges)
        values = [0] * n
        for i in range(n):
            x = edges[i]
            values[x] += i

        res = max(values)
        for i in range(n):
            if values[i] == res:
                return i
        return -1


if __name__ == '__main__':
    pass
