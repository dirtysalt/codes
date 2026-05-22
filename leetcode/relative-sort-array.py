#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        pos = {k: idx for (idx, k) in enumerate(arr2)}
        arr1.sort(key=lambda x: (pos.get(x, len(arr2)), x))
        return arr1
