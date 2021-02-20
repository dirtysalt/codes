#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt
from collections import Counter

from typing import List


class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        import heapq

        from collections import defaultdict
        last = defaultdict(list)

        for x in nums:
            # query last
            pq = last[x - 1]
            y = heapq.heappop(pq) if pq else 0
            heapq.heappush(last[x], y + 1)

        for x, pq in last.items():
            if pq and pq[0] < 3:
                return False
        return True


cases = [
    ([1, 2, 3, 3, 4, 5], True),
    ([1, 2, 3, 3, 4, 4, 5, 5], True),
    ([1, 2, 3, 4, 4, 5], False),
]

import aatest_helper

aatest_helper.run_test_cases(Solution().isPossible, cases)
