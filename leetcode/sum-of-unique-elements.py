#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        from collections import Counter
        cnt = Counter(nums)
        ans = 0
        for x in nums:
            if cnt[x] == 1:
                ans += x
        return ans
