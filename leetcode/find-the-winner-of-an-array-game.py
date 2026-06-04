#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        from collections import deque
        dq = deque()
        for x in arr:
            dq.append(x)
        n = len(arr)

        ok = 0
        while ok < k and ok < (n - 1):
            x = dq.popleft()
            y = dq.popleft()
            if x > y:
                dq.appendleft(x)
                dq.append(y)
                ok += 1
            else:
                dq.appendleft(y)
                dq.append(x)
                ok = 1
        return dq.popleft()


cases = [
    ([2, 1, 3, 5, 4, 6, 7], 2, 5),
    ([3, 2, 1], 10, 3),
    ([1, 9, 8, 2, 3, 7, 6, 4, 5], 7, 9),
    ([1, 11, 22, 33, 44, 55, 66, 77, 88, 99], 1000000000, 99,),
]

import aatest_helper

aatest_helper.run_test_cases(Solution().getWinner, cases)
