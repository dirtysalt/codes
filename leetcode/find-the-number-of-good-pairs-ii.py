#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], k: int) -> int:
        from collections import Counter
        cnt1 = Counter([x // k for x in nums1 if x % k == 0])
        if not cnt1: return 0
        U = max(cnt1)

        ans = 0
        for i, c in Counter(nums2).items():
            for j in range(i, U + 1, i):
                ans += cnt1[j] * c
        return ans


if __name__ == '__main__':
    pass
