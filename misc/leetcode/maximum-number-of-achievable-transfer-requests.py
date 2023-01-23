#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def maximumRequests(self, n: int, requests: List[List[int]]) -> int:

        def dfs(k, st):
            if k == len(requests):
                if all((x == 0 for x in st)):
                    return 0
                return -(1 << 30)

            a, b = requests[k]
            t0 = dfs(k + 1, st)
            st[a] -= 1
            st[b] += 1
            t1 = dfs(k + 1, st) + 1
            st[a] += 1
            st[b] -= 1
            return max(t0, t1)

        st = [0] * n
        ans = dfs(0, st)
        return ans


cases = [
    (5, [[0, 1], [1, 0], [0, 1], [1, 2], [2, 0], [3, 4]], 5),
    (3, [[0, 0], [1, 2], [2, 1]], 3),
    (4, [[0, 3], [3, 1], [1, 2], [2, 0]], 4)
]
import aatest_helper

aatest_helper.run_test_cases(Solution().maximumRequests, cases)
