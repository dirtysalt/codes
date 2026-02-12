#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt
import random
from typing import List


class Solution:
    def getMinDistSum(self, positions: List[List[int]]) -> float:
        step = 100

        xs = [x[0] for x in positions]
        ys = [x[1] for x in positions]
        n = len(positions)
        xc = sum(xs) / n
        yc = sum(ys) / n

        def dist(xc, yc):
            res = 0
            for i in range(n):
                t0 = (xc - xs[i]) ** 2
                t1 = (yc - ys[i]) ** 2
                res += (t0 + t1) ** 0.5
            return res

        while step > 1e-7:
            iter = False
            for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                xc2 = xc + dx * step
                yc2 = yc + dy * step
                if dist(xc2, yc2) < dist(xc, yc):
                    iter = True
                    xc, yc = xc2, yc2
                    break
            if not iter:
                step = step / 2

        ans = round(dist(xc, yc), 5)
        return ans


class Solution2:
    def getMinDistSum(self, positions: List[List[int]]) -> float:
        decay = 1 - 0.001
        batchSize = 100
        eps = 1e-7
        alpha = 1

        xs = [x[0] for x in positions]
        ys = [x[1] for x in positions]
        n = len(positions)
        xc = sum(xs) / n
        yc = sum(ys) / n

        def dist(xc, yc):
            res = 0
            for i in range(n):
                t0 = (xc - xs[i]) ** 2
                t1 = (yc - ys[i]) ** 2
                res += (t0 + t1) ** 0.5
            return res

        value = dist(xc, yc)
        while True:
            random.shuffle(positions)
            dx, dy = 0, 0
            for i in range(min(n, batchSize)):
                d = ((xc - xs[i]) ** 2 + (yc - ys[i]) ** 2) ** 0.5
                dx += (xc - xs[i]) / (d + eps)
                dy += (yc - ys[i]) / (d + eps)

            xc -= alpha * dx
            yc -= alpha * dy
            alpha *= decay

            newValue = dist(xc, yc)
            if abs(newValue - value) < 1e-7:
                break
            value = newValue

        ans = round(value, 5)
        return ans


cases = [
    ([[0, 1], [3, 2], [4, 5], [7, 6], [8, 9], [11, 1], [2, 12]], 32.94036),
    ([[1, 1], [0, 0], [2, 0]], 2.73205),
    ([[1, 1], [3, 3]], 2.82843),
    ([[44, 23], [18, 45], [6, 73], [0, 76], [10, 50], [30, 7], [92, 59], [44, 59], [79, 45], [69, 37], [66, 63],
      [10, 78], [88, 80], [44, 87]], 499.28078),
]
import aatest_helper

aatest_helper.run_test_cases(Solution2().getMinDistSum, cases)
