#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        arr = list(zip(startTime, endTime, profit))
        arr.sort(key=lambda x: (x[1], x[0]))

        tmp = [(0, 0)]

        def bs(v):
            s, e = 0, len(tmp) - 1
            while s <= e:
                m = (s + e) // 2
                if tmp[m][0] == v:
                    return m
                if tmp[m][0] > v:
                    e = m - 1
                else:
                    s = m + 1
            return e

        for s, e, p in arr:
            idx = bs(s)
            e0, p0 = tmp[-1]
            p1 = tmp[idx][1] + p
            if p1 > p0:
                if e == e0:
                    tmp[-1] = (e, p1)
                else:
                    tmp.append((e, p1))

        # ans = max([x[1] for x in tmp])
        ans = tmp[-1][1]
        return ans


cases = [
    ([1, 2, 3, 3], [3, 4, 5, 6], [50, 10, 40, 70], 120),
    ([1, 2, 3, 4, 6], [3, 5, 10, 6, 9], [20, 20, 100, 70, 60], 150),
    ([1, 1, 1], [2, 3, 4], [5, 6, 4], 6)
]

import aatest_helper

aatest_helper.run_test_cases(Solution().jobScheduling, cases)
