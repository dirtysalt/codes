#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List
from collections import Counter, defaultdict, deque
from functools import lru_cache
import heapq


class Solution:
    def countServers(self, n: int, logs: List[List[int]], x: int, queries: List[int]) -> List[int]:
        logs.sort(key=lambda x: (x[1], x[0]))
        qs = [(q, idx) for (idx, q) in enumerate(queries)]
        qs.sort()

        from collections import Counter
        cnt = Counter()
        ans = [0] * len(queries)

        s, e = 0, 0

        for q, idx in qs:
            begin, end = q - x, q

            while e < len(logs) and logs[e][1] <= end:
                server = logs[e][0]
                cnt[server] += 1
                e += 1

            while s < len(logs) and logs[s][1] < begin:
                server = logs[s][0]
                cnt[server] -= 1
                if cnt[server] == 0:
                    del cnt[server]
                s += 1

            ans[idx] = (n - len(cnt))

        return ans


true, false, null = True, False, None
import aatest_helper

cases = [
    (3, [[1, 3], [2, 6], [1, 5]], 5, [10, 11], [1, 2]),
    (3, [[2, 4], [2, 1], [1, 2], [3, 1]], 2, [3, 4], [0, 1]),
]

aatest_helper.run_test_cases(Solution().countServers, cases)

if __name__ == '__main__':
    pass
