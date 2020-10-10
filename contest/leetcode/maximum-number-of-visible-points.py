#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def visiblePoints(self, points: List[List[int]], angle: int, location: List[int]) -> int:
        import math

        pi = math.pi

        def computeAngle(x, y, ox, oy):
            dy = y - oy
            dx = x - ox
            if dx == 0:
                if dy > 0:
                    return 90
                else:
                    return 270

            v = math.atan2(dy, dx)
            if v < -pi / 2:
                v += 2 * pi
            v = v / (2 * pi) * 360
            return v

        same = 0
        arr = []
        ox, oy = location
        for x, y in points:
            if x == ox and y == oy:
                same += 1
                continue
            arr.append(computeAngle(x, y, ox, oy))
        arr.sort()
        # print(arr)
        arr = arr + [x + 360 for x in arr]

        ans = 0
        j = 0
        for i in range(len(arr)):
            while arr[i] - arr[j] > angle:
                j += 1
            ans = max(ans, i - j + 1)
        ans += same
        return ans


cases = [
    ([[2, 1], [2, 2], [3, 3]], 90, [1, 1], 3),
    ([[2, 1], [2, 2], [3, 4], [1, 1]], 90, [1, 1], 4),
    ([[1, 0], [2, 1]], 13, [1, 1], 1),
]

import aatest_helper

aatest_helper.run_test_cases(Solution().visiblePoints, cases)
