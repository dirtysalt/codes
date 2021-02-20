#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        ans = []
        from collections import defaultdict
        res = defaultdict(list)
        for i in range(len(nums)):
            for j in range(len(nums[i])):
                res[i + j].append(nums[i][j])

        keys = sorted(res.keys())
        for k in keys:
            ans.extend(res[k][::-1])
        return ans
