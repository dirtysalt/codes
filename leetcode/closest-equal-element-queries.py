#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def solveQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        from sortedcontainers import SortedList
        from collections import defaultdict
        d = defaultdict(lambda: SortedList())

        for i in range(len(nums)):
            d[nums[i]].add(i)

        ans = []
        for q in queries:
            x = nums[q]
            if len(d[x]) == 1:
                ans.append(-1)
                continue

            dx = d[x]
            idx = dx.bisect_left(q)
            # print(q, dx, idx)
            dist = (1 << 30)

            def D(a, b):
                if a > b:
                    a, b = b, a
                return min(b - a, (a + len(nums) - b))

            p = dx[idx - 1]
            dist = min(dist, D(p, q))
            p = dx[(idx + 1) % len(dx)]
            dist = min(dist, D(p, q))

            ans.append(dist)
        return ans


true, false, null = True, False, None
import aatest_helper

cases = [
    aatest_helper.OrderedDict(nums=[1, 3, 1, 4, 1, 3, 2], queries=[0, 3, 5], res=[2, -1, 3]),
    aatest_helper.OrderedDict(nums=[1, 2, 3, 4], queries=[0, 1, 2, 3], res=[-1, -1, -1, -1])
]

aatest_helper.run_test_cases(Solution().solveQueries, cases)

if __name__ == '__main__':
    pass
