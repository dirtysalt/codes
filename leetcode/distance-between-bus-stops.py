#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        k = start
        x = 0
        n = len(distance)
        for i in range(n):
            x += distance[k]
            k = (k+1) % n
            if k == destination:
                break
        tt = sum(distance)
        ans = min(x, tt - x)
        return ans
