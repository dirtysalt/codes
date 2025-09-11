#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List
from collections import Counter, defaultdict, deque
from functools import lru_cache
import heapq


class Solution:
    def countBeautifulPairs(self, nums: List[int]) -> int:

        def gcd(x, y):
            while y != 0:
                x, y = y, x % y
            return x

        n = len(nums)
        ans = 0
        for i in range(n):
            for j in range(i + 1, n):
                a = int(str(nums[i])[0])
                b = nums[j] % 10
                if gcd(a, b) == 1:
                    ans += 1
        return ans


if __name__ == '__main__':
    pass
