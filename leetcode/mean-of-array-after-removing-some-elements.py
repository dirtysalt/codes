#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def trimMean(self, arr: List[int]) -> float:
        arr.sort()
        n = len(arr)
        s = 0
        c = 0
        k, j = int(n * 0.05) - 1, int(n * 0.95)
        # print(k, j)
        for i in range(n):
            if i > k and i < j:
                s += arr[i]
                c += 1
        avg = s / c
        return avg
