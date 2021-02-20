#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


# https://leetcode.com/problems/beautiful-array/discuss/186679/Odd-%2B-Even-Pattern-O(N)
# clear explanation and solution.

class Solution:
    def beautifulArray(self, N: int) -> List[int]:
        res = [1]
        while len(res) < N:
            a = [2 * x - 1 for x in res if (2 * x - 1) <= N]
            b = [2 * x for x in res if (2 * x) <= N]
            res = a + b
        return res
