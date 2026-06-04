#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def canChoose(self, groups: List[List[int]], nums: List[int]) -> bool:

        import functools
        @functools.lru_cache()
        def match(i, j):
            if i == len(groups): return True
            if j == len(nums): return False

            k = j
            ok = True
            for x in groups[i]:
                if k == len(nums) or nums[k] != x:
                    ok = False
                    break
                k += 1

            if ok:
                return match(i + 1, k)
            else:
                return match(i, j + 1)

        ans = match(0, 0)
        return ans
