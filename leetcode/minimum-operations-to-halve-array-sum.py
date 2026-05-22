#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def halveArray(self, nums: List[int]) -> int:
        t = sum(nums)
        T = t / 2
        import heapq
        hp = [-x for x in nums]
        heapq.heapify(hp)
        ans = 0
        while t > T:
            x = -heapq.heappop(hp)
            half = x / 2
            t -= half
            heapq.heappush(hp, -half)
            ans += 1
        return ans


true, false, null = True, False, None
cases = [
    ([3, 8, 20], 3),
    ([5, 19, 8, 1], 3),
]

import aatest_helper

aatest_helper.run_test_cases(Solution().halveArray, cases)

if __name__ == '__main__':
    pass
