#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        count = [0, 0]
        zero, one = 0, 0
        for x in students:
            count[x] += 1

        from collections import deque
        dq = deque()
        for x in students:
            dq.append(x)

        for x in sandwiches:
            if count[x] == 0: break
            count[x] -= 1
            while dq[0] != x:
                t = dq.popleft()
                dq.append(t)

        ans = count[0] + count[1]
        return ans


cases = [
    ([1, 1, 0, 0], [0, 1, 0, 1], 0),
    ([1, 1, 1, 0, 0, 1], [1, 0, 0, 0, 1, 1], 3),
]

import aatest_helper

aatest_helper.run_test_cases(Solution().countStudents, cases)
