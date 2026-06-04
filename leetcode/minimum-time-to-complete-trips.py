#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List

class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:

        def test(T):
            res = 0
            for t in time:
                res += T // t
            return res >= totalTrips

        s, e = 0, max(time) * totalTrips
        while s <= e:
            m = (s + e) // 2
            if test(m):
                e = m - 1
            else:
                s = m + 1
        return s

if __name__ == '__main__':
    pass
