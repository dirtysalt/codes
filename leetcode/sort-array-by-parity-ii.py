#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        n = len(A)
        ans = [0] * n
        i, j = 0, 1
        for v in A:
            if v % 2 == 0:
                ans[i] = v
                i += 2
            else:
                ans[j] = v
                j += 2
        return ans
