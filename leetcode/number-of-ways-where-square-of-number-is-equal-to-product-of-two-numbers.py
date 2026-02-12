#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:

        def test(xs, ys):
            from collections import Counter
            cnt = Counter()
            for y in ys:
                cnt[y * y] += 1

            n = len(xs)
            ans = 0
            for i in range(n):
                for j in range(i + 1, n):
                    z = xs[i] * xs[j]
                    ans += cnt[z]
            return ans

        ans = 0
        ans += test(nums1, nums2)
        ans += test(nums2, nums1)
        return ans
