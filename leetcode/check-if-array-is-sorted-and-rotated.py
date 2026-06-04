#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def check(self, nums: List[int]) -> bool:
        tmp = nums + nums
        n = len(nums)
        for i in range(n):
            ok = True
            for j in range(1, n):
                if tmp[i + j] < tmp[i + j - 1]:
                    ok = False
                    break
            if ok:
                return True
        return False
