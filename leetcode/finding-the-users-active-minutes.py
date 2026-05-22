#!/usr/bin/env python3
# coding:utf-8
# Copyright (C) dirlt

from typing import List
from collections import Counter, defaultdict, deque
from functools import lru_cache
import heapq

class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
        # sort by (time, id)
        logs.sort(key = lambda x: (x[1], x[0]))

        from collections import Counter
        idc = Counter()
        prev = logs[0]

        for t in logs:
            if t == prev:
                continue

            idc[prev[0]] += 1
            prev = t

        idc[prev[0]] += 1

        ans = [0] * k
        for c in idc.values():
            ans[c-1] += 1
        return ans

cases = [
    ([[0,5],[1,2],[0,2],[0,5],[1,3]], 5, [0,2,0,0,0]),
    ([[1,1],[2,2],[2,3]], 4, [1,1,0,0]),
]

import aatest_helper
aatest_helper.run_test_cases(Solution().findingUsersActiveMinutes, cases)


if __name__ == '__main__':
    pass
