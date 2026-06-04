#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
        pq = []
        import heapq
        ans = []
        i = 0
        lastP = -1
        while len(ans) != k:
            while (len(nums) - i) + len(ans) >= k:
                heapq.heappush(pq, (nums[i], i))
                i += 1

            while pq[0][1] < lastP:
                heapq.heappop(pq)

            x, p = heapq.heappop(pq)
            ans.append(x)
            lastP = p

        assert len(ans) == k
        return ans


cases = [
    ([3, 5, 2, 6], 2, [2, 6]),
    ([2, 4, 3, 3, 5, 4, 9, 6], 4, [2, 3, 3, 4]),
    ([71, 18, 52, 29, 55, 73, 24, 42, 66, 8, 80, 2], 3, [8, 80, 2]),
    ([84, 10, 71, 23, 66, 61, 62, 64, 34, 41, 80, 25, 91, 43, 4, 75, 65, 13, 37, 41, 46, 90, 55, 8, 85, 61, 95, 71],
     24, [10, 23, 61, 62, 34, 41, 80, 25, 91, 43, 4, 75, 65, 13, 37, 41, 46, 90, 55, 8, 85, 61, 95, 71])
]

import aatest_helper

aatest_helper.run_test_cases(Solution().mostCompetitive, cases)
