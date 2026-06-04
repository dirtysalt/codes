#!/usr/bin/env python3
# coding:utf-8
# Copyright (C) dirlt

from typing import List
from collections import Counter, defaultdict, deque
from functools import lru_cache
import heapq

class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        tasks = [(i, tasks[i][0], tasks[i][1]) for i in range(len(tasks))]
        # sort by enqueue time and reverse.
        tasks.sort(key = lambda x: x[1], reverse = True)

        hp = []
        t = 0
        ans = []
        while True:
            if tasks and tasks[-1][1] > t and not hp:
                t = tasks[-1][1]

            while tasks and tasks[-1][1] <= t:
                (i, et, pt) = tasks.pop()
                heapq.heappush(hp, (pt, i, et))

            if not hp: break
            (pt, i, et) = heapq.heappop(hp)
            ans.append(i)
            t = max(t, et)
            t += pt
        return ans

cases = [
    ( [[1,2],[2,4],[3,2],[4,1]], [0,2,3,1]),
    ([[7,10],[7,12],[7,5],[7,4],[7,2]],[4,3,2,0,1]),
    ([[35,36],[11,7],[15,47],[34,2],[47,19],[16,14],[19,8],[7,34],[38,15],[16,18],[27,22],[7,15],[43,2],[10,5],[5,4],[3,11]], [15,14,13,1,6,3,5,12,8,11,9,4,10,7,0,2]),
]

import aatest_helper
aatest_helper.run_test_cases(Solution().getOrder, cases)


if __name__ == '__main__':
    pass
