#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        n = len(s)
        arr = list(s)
        for i in range(n):
            c, p = s[i], indices[i]
            arr[p] = c
        ans = ''.join(arr)
        return ans
