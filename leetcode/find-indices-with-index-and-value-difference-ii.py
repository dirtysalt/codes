#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def findIndices(self, nums: List[int], indexDifference: int, valueDifference: int) -> List[int]:
        from sortedcontainers import SortedList
        sl = SortedList()
        for i in range(indexDifference, len(nums)):
            sl.add((nums[i], i))

        def find(a, b):
            pos = []
            j = sl.bisect_left((a, len(nums)))
            pos.extend([j - 1, j])
            j = sl.bisect_right((b, -1))
            pos.extend([j, j + 1])
            pos = [p for p in pos if 0 <= p < len(sl)]
            # print(a, b, [sl[p] for p in pos])
            for p in pos:
                v, j = sl[p]
                if v <= a or v >= b:
                    return j
            return -1

        for i in range(len(nums)):
            if not sl: break
            # nums[j] <= (nums[i] - valueDiff)
            # or nums[j] >= (nums[i] + valueDiff)
            j = find(nums[i] - valueDifference, nums[i] + valueDifference)
            if j != -1: return [i, j]
            sl.remove((nums[i + indexDifference], i + indexDifference))
        return [-1, -1]


true, false, null = True, False, None
import aatest_helper

cases = [
    aatest_helper.OrderedDict(nums=[5, 1, 4, 1], indexDifference=2, valueDifference=4, res=[0, 3]),
    aatest_helper.OrderedDict(nums=[2, 1], indexDifference=0, valueDifference=0, res=[0, 0]),
    aatest_helper.OrderedDict(nums=[1, 2, 3], indexDifference=2, valueDifference=4, res=[-1, -1]),
]

aatest_helper.run_test_cases(Solution().findIndices, cases)

if __name__ == '__main__':
    pass
