#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def smallestRepunitDivByK(self, K: int) -> int:
        i = 0
        n = 0
        visited = set()
        while True:
            i = i + 1
            n = (n * 10 + 1) % K
            if n == 0:
                break
            if n in visited:
                return -1
            visited.add(n)
        return i
