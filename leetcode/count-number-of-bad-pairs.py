#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        from collections import Counter
        c = Counter()
        n = len(nums)
        for i in range(n):
            d = nums[i] - i
            c[d] += 1

        ans = 0
        for i in range(n):
            d = nums[i] - i
            x = n - c[d]
            ans += x

        return ans // 2


if __name__ == '__main__':
    pass
