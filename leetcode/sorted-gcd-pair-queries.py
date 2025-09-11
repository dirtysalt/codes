#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt
from bisect import bisect_right
from itertools import accumulate
from typing import List


class Solution:
    def gcdValues(self, nums: List[int], queries: List[int]) -> List[int]:
        mx = max(nums)
        cnt_x = [0] * (mx + 1)
        cnt_gcd = [0] * (mx + 1)
        for x in nums:
            cnt_x[x] += 1

        for i in range(mx, 0, -1):
            c = 0
            dup = 0
            for j in range(i, mx + 1, i):
                c += cnt_x[j]
                dup += cnt_gcd[j]
            cnt_gcd[i] = c * (c - 1) // 2 - dup

        s = list(accumulate(cnt_gcd))
        ans = [bisect_right(s, q) for q in queries]
        return ans


true, false, null = True, False, None
import aatest_helper

cases = [
    ([2, 3, 4], [0, 2, 2], [1, 2, 2]),
    ([4, 4, 2, 1], [5, 3, 1, 0], [4, 2, 1, 1]),
    ([2, 2], [0, 0], [2, 2])
]

aatest_helper.run_test_cases(Solution().gcdValues, cases)

if __name__ == '__main__':
    pass
