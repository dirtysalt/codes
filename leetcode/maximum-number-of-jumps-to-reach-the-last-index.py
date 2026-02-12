#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List
from collections import Counter, defaultdict, deque
from functools import lru_cache
import heapq


class Solution:
    def maximumJumps(self, nums: List[int], target: int) -> int:
        n = len(nums)
        dp = [-1] * n
        dp[0] = 0

        for i in range(n):
            if dp[i] == -1: continue
            for j in range(i + 1, n):
                if -target <= (nums[j] - nums[i]) <= target:
                    dp[j] = max(dp[j], dp[i] + 1)

        # print(dp)
        return dp[-1]


if __name__ == '__main__':
    pass
