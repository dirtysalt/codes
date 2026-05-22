#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt
from typing import List


class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        ans = 0

        res = sum(arr[:k])
        t = threshold * k
        if res >= t:
            ans += 1

        for i in range(k, len(arr)):
            res += arr[i] - arr[i - k]
            if res >= t:
                ans += 1

        return ans
