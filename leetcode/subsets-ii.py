#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        from collections import Counter
        cnt = Counter(nums)
        ans = [[]]

        for x, c in cnt.items():
            tmp = []
            for s in ans:
                for j in range(1, c + 1):
                    tmp.append(s + [x] * j)
            ans.extend(tmp)

        return ans
