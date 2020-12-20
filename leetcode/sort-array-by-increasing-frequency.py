#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        from collections import Counter
        cnt = Counter()
        for x in nums:
            cnt[x] += 1

        ans = nums
        ans.sort(key=lambda x: (cnt[x], -x))
        return ans
