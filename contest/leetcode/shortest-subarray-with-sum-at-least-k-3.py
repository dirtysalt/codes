#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def shortestSubarray(self, A: List[int], K: int) -> int:
        from collections import deque

        dq = deque()
        dq.append((0, -1))

        n = len(A)
        ans = n + 1
        acc = 0
        for i in range(n):
            acc += A[i]

            while dq and (acc - dq[0][0]) >= K:
                ans = min(ans, i - dq[0][1])
                dq.popleft()

            while dq and acc <= dq[-1][0]:
                dq.pop()
            dq.append((acc, i))

        if ans == (n + 1):
            ans = -1
        return ans


cases = [
    ([17, 85, 93, -45, -21], 150, 2)
]

import aatest_helper

aatest_helper.run_test_cases(Solution().shortestSubarray, cases)
