#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def countMatchingSubarrays(self, nums: List[int], pattern: List[int]) -> int:
        n, m = len(nums), len(pattern)
        P = [0] * (n - 1)
        for i in range(1, n):
            d = nums[i] - nums[i - 1]
            if d > 0: d = 1
            if d < 0: d = -1
            P[i - 1] = d

        ans = 0
        for i in range(0, n - m):
            if P[i:i + m] == pattern:
                ans += 1

        return ans


if __name__ == '__main__':
    pass
