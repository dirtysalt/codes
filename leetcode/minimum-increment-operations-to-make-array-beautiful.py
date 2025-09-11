#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt
import functools
from typing import List


class Solution:
    def minIncrementOperations(self, nums: List[int], k: int) -> int:
        INF = k * len(nums)

        @functools.cache
        def cover(i, j):
            if j == len(nums): return 0
            ans = INF
            if j < (i + 3):
                ans = min(ans, cover(i, j + 1))

            c = max(k - nums[j], 0)
            ans = min(ans, c + cover(j, j + 1))
            return ans

        return cover(-1, 0)


if __name__ == '__main__':
    pass
