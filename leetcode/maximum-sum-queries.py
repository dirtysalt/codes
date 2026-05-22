#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt
from bisect import bisect_left
from typing import List


class Solution:
    def maximumSumQueries(self, nums1: List[int], nums2: List[int], queries: List[List[int]]) -> List[int]:
        Q = []
        for x, y in zip(nums1, nums2):
            Q.append((x, y, -1))
        for idx in range(len(queries)):
            x, y = queries[idx]
            Q.append((x, y, idx))
        Q.sort(key=lambda x: (-x[0], -x[1], x[2]))

        ans = [0] * len(queries)
        st = []

        def update(y, value):
            # value 递减，y 递增
            while st and st[-1][1] <= value:
                st.pop()
            if not st or st[-1][0] < y:
                st.append((y, value))

        def find(y):
            idx = bisect_left(st, (y,))
            if idx < len(st):
                return st[idx][1]
            return -1

        for (x, y, idx) in Q:
            if idx == -1:
                update(y, x + y)
            else:
                value = find(y)
                ans[idx] = value
        return ans


true, false, null = True, False, None
import aatest_helper

cases = [
    ([4, 3, 1, 2], [2, 4, 9, 5], [[4, 1], [1, 3], [2, 5]], [6, 10, 7]),
    ([3, 2, 5], [2, 3, 4], [[4, 4], [3, 2], [1, 1]], [9, 9, 9]),
    ([2, 1], [2, 3], [[3, 3]], [-1]),
    ([30, 82, 10], [94, 57, 54], [[28, 50]], [139]),
    ([30, 82, 10], [94, 57, 54], [[6, 1], [78, 97], [28, 50]], [139, -1, 139]),
    ([35, 69], [63, 21], [[59, 93], [20, 8]], [-1, 98]),
    ([77, 79], [70, 53], [[16, 29], [14, 9], [21, 96], [5, 53], [91, 90]], [147, 147, -1, 147, -1]),
]

aatest_helper.run_test_cases(Solution().maximumSumQueries, cases)

if __name__ == '__main__':
    pass
