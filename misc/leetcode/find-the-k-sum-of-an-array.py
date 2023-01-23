#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt
from typing import List


class Solution:
    def kSum(self, nums: List[int], k: int) -> int:
        a = [x for x in nums if x >= 0]
        base = sum(a)
        a += [-x for x in nums if x < 0]
        a.sort()

        import heapq
        hp = [(0, -1)]
        for step in range(k - 1):
            value, idx = heapq.heappop(hp)
            for i in range(k - step):
                j = idx + 1 + i
                if j < len(a):
                    heapq.heappush(hp, (value + a[j], j))
                else:
                    break
        ans = base - hp[0][0]
        return ans


true, false, null = True, False, None
cases = [
    ([2, 4, -2], 5, 2),
    ([1, -2, 3, 4, -10, 12], 16, 10),
    ([1000, 1001, 1002, 1003, 1004, 1005, 1006, 1007, 1008, 1009], 10, 9037),
]
import aatest_helper

aatest_helper.run_test_cases(Solution().kSum, cases)

if __name__ == '__main__':
    pass
