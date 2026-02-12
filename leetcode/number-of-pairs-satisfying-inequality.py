#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], diff: int) -> int:
        # nums1[i] - nums1[j] <= nums2[i] - nums2[j] + diff.
        # nums1[i] - nums2[i] <= nums1[j] - nums2[j] + diff

        n = len(nums2)
        from sortedcontainers import SortedList
        sl = SortedList()
        for i in range(n):
            sl.add(nums1[i] - nums2[i])

        ans = 0
        for i in range(n):
            v = nums1[i] - nums2[i]
            sl.remove(v)
            exp = v - diff
            # >= exp
            j = sl.bisect_left(exp)
            ans += len(sl) - j
        return ans


if __name__ == '__main__':
    pass
