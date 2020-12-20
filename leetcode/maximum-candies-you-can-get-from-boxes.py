#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def maxCandies(self, status: List[int], candies: List[int], keys: List[List[int]], containedBoxes: List[List[int]],
                   initialBoxes: List[int]) -> int:
        n = len(status)
        visit = [0] * n
        st = status.copy()
        wait = set()

        ans = 0
        from collections import deque
        dq = deque()
        for b in initialBoxes:
            if status[b] == 1:
                dq.append(b)
                visit[b] = 1
            else:
                wait.add(b)

        while dq:
            b = dq.popleft()
            ans += candies[b]

            changed = []
            for k in keys[b]:
                st[k] = 1
                if k in wait:
                    changed.append(k)

            for cb in containedBoxes[b]:
                wait.add(cb)
                if st[cb] == 1:
                    changed.append(cb)

            for x in changed:
                if visit[x] == 0:
                    visit[x] = 1
                    dq.append(x)
                    wait.remove(x)
        return ans


cases = [
    ([1, 0, 1, 0], [7, 5, 4, 100], [[], [], [1], []], [[1, 2], [3], [], []], [0], 16),
    ([1, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 1], [[1, 2, 3, 4, 5], [], [], [], [], []],
     [[1, 2, 3, 4, 5], [], [], [], [], []], [0], 6)
]

import aatest_helper

aatest_helper.run_test_cases(Solution().maxCandies, cases)
