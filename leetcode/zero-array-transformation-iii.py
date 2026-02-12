#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt
import heapq
from typing import List


class Solution:
    def maxRemoval(self, nums: List[int], queries: List[List[int]]) -> int:
        n = len(nums)

        queries.sort()
        diff = [0] * (n + 1)
        h = []
        sum_d, j = 0, 0
        for i, x in enumerate(nums):
            sum_d += diff[i]

            # add query end into heap
            while j < len(queries) and queries[j][0] <= i:
                heapq.heappush(h, -queries[j][1])
                j += 1

            while sum_d < x and h and -h[0] >= i:
                diff[-h[0] + 1] -= 1
                sum_d += 1
                heapq.heappop(h)

            if sum_d < x:
                return -1
        return len(h)


true, false, null = True, False, None
import aatest_helper

cases = [
    aatest_helper.OrderedDict(nums=[2, 0, 2], queries=[[0, 2], [0, 2], [1, 1]], res=1),
    aatest_helper.OrderedDict(nums=[1, 1, 1, 1], queries=[[1, 3], [0, 2], [1, 3], [1, 2]], res=2),
    aatest_helper.OrderedDict(nums=[1, 2, 3, 4], queries=[[0, 3]], res=-1),
]

aatest_helper.run_test_cases(Solution().maxRemoval, cases)

if __name__ == '__main__':
    pass
