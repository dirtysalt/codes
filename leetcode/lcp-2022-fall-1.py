#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def temperatureTrend(self, temperatureA: List[int], temperatureB: List[int]) -> int:
        ta = temperatureA
        tb = temperatureB
        n = len(ta)

        def diff(x):
            if x > 0:
                return 1
            elif x < 0:
                return -1
            return 0

        ans = 0
        t = 0
        for i in range(1, n):
            a = diff(ta[i] - ta[i - 1])
            b = diff(tb[i] - tb[i - 1])
            if a == b:
                t += 1
            else:
                ans = max(ans, t)
                t = 0
        ans = max(ans, t)
        return ans


if __name__ == '__main__':
    pass
