#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def getSubarrayBeauty(self, nums: List[int], k: int, x: int) -> List[int]:
        from sortedcontainers import SortedList
        sl = SortedList(nums[:k])
        ans = []
        v = min(sl[x - 1], 0)
        ans.append(v)
        for i in range(k, len(nums)):
            sl.remove(nums[i - k])
            sl.add(nums[i])
            v = min(sl[x - 1], 0)
            ans.append(v)
        return ans


if __name__ == '__main__':
    pass
