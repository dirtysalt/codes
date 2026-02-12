#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List
from collections import Counter, defaultdict, deque
from functools import lru_cache
import heapq


class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        def bits(x):
            if x == 0:
                return 0, 1
            a, b = 0, 0

            while x:
                if x & 0x1:
                    a += 1
                else:
                    b += 1
                x = x // 2
            return a, b

        right = 0
        for x in nums:
            a, b = bits(x)
            right += a
        left = 0
        ans = [right]

        for i in range(len(nums)):
            a, b = bits(nums[i])
            right -= a
            left += b
            ans.append(left + right)

        # print(ans)
        v = max(ans)
        res = []
        for i in range(len(nums) + 1):
            if ans[i] == v:
                res.append(i)
        return res


if __name__ == '__main__':
    pass
