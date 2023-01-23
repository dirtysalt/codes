#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def maximumSegmentSum(self, nums: List[int], removeQueries: List[int]) -> List[int]:
        n = len(nums)
        acc = [0] * (n + 1)
        for i in range(n):
            acc[i + 1] = acc[i] + nums[i]

        from sortedcontainers import SortedList
        rs = SortedList()
        values = SortedList()
        rs.add((0, n))
        values.add((acc[-1]))

        ans = []
        for x in removeQueries:
            idx = rs.bisect((x, 1 << 30))
            lo, hi = rs[idx - 1]
            rs.remove((lo, hi))

            v = acc[hi] - acc[lo]
            values.remove(v)

            rs2 = [(lo, x), (x + 1, hi)]
            for a, b in rs2:
                if a < b:
                    v = acc[b] - acc[a]
                    values.add(v)
                    rs.add((a, b))

            ans.append(values[-1] if values else 0)
        return ans


true, false, null = True, False, None
cases = [
    ([1, 2, 5, 6, 1], [0, 3, 2, 4, 1], [14, 7, 2, 2, 0]),
    ([3, 2, 11, 1], [3, 2, 1, 0], [16, 5, 3, 0]),
    ([500, 822, 202, 707, 298, 484, 311, 680, 901, 319, 343, 340], [6, 4, 0, 5, 2, 3, 10, 8, 7, 9, 1, 11],
     [3013, 2583, 2583, 2583, 2583, 2583, 1900, 822, 822, 822, 340, 0]),
]

import aatest_helper

aatest_helper.run_test_cases(Solution().maximumSegmentSum, cases)

if __name__ == '__main__':
    pass
