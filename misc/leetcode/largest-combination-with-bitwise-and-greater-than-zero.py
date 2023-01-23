#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List

class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        bits = [0] * 24

        for c in candidates:
            for i in range(24):
                if c & (1 << i):
                    bits[i] += 1

        return max(bits)

if __name__ == '__main__':
    pass
