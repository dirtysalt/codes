#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt
import math
from typing import List


class GeometryUtil:
    @staticmethod
    def TwoLinesCrossPoint(line1, line2, onLine=True):
        # https://zhuanlan.zhihu.com/p/138718555
        point_is_exist = False
        x = y = 0
        x1, y1, x2, y2 = line1
        x3, y3, x4, y4 = line2

        if (x2 - x1) == 0:
            k1 = None
            b1 = 0
        else:
            k1 = (y2 - y1) * 1.0 / (x2 - x1)  # 计算k1,由于点均为整数，需要进行浮点数转化
            b1 = y1 * 1.0 - x1 * k1 * 1.0  # 整型转浮点型是关键

        if (x4 - x3) == 0:  # L2直线斜率不存在
            k2 = None
            b2 = 0
        else:
            k2 = (y4 - y3) * 1.0 / (x4 - x3)  # 斜率存在
            b2 = y3 * 1.0 - x3 * k2 * 1.0

        if k1 is None:
            if not k2 is None:
                x = x1
                y = k2 * x1 + b2
                point_is_exist = True
        elif k2 is None:
            x = x3
            y = k1 * x3 + b1
        elif not k2 == k1:
            x = (b2 - b1) * 1.0 / (k1 - k2)
            y = k1 * x * 1.0 + b1 * 1.0
            point_is_exist = True

        if point_is_exist:
            p = [x, y]
            if onLine and GeometryUtil.PointOnLine(p, line1, line2):
                return [x, y]
        return []

    @staticmethod
    def PointOnLine(p, l, l2):
        x, y = p
        x1, y1, x2, y2 = l
        if not (min(x1, x2) <= x <= max(x1, x2) and min(y1, y2) <= y <= max(y1, y2)):
            return []
        x1, y1, x2, y2 = l2
        if not (min(x1, x2) <= x <= max(x1, x2) and min(y1, y2) <= y <= max(y1, y2)):
            return []
        return p

    @staticmethod
    def LineIntersectCircle(p, l):
        # https://www.codingdict.com/questions/187334
        x0, y0, r0 = p
        x1, y1, x2, y2 = l
        if x1 == x2:
            if abs(r0) >= abs(x1 - x0):
                p1 = x1, y0 - math.sqrt(r0 ** 2 - (x1 - x0) ** 2)
                p2 = x1, y0 + math.sqrt(r0 ** 2 - (x1 - x0) ** 2)
                inp = [p1, p2]
                # select the points lie on the line segment
                inp = [p for p in inp if min(y1, y2) <= p[1] <= max(y1, y2)]
            else:
                inp = []
        else:
            k = (y1 - y2) / (x1 - x2)
            b0 = y1 - k * x1
            a = k ** 2 + 1
            b = 2 * k * (b0 - y0) - 2 * x0
            c = (b0 - y0) ** 2 + x0 ** 2 - r0 ** 2
            delta = b ** 2 - 4 * a * c
            if delta >= 0:
                p1x = (-b - math.sqrt(delta)) / (2 * a)
                p2x = (-b + math.sqrt(delta)) / (2 * a)
                p1y = k * x1 + b0
                p2y = k * x2 + b0
                inp = [[p1x, p1y], [p2x, p2y]]
                # select the points lie on the line segment
                inp = [p for p in inp if min(x1, x2) <= p[0] <= max(x1, x2)]
            else:
                inp = []
        return inp

    @staticmethod
    def TwoCirclesCrossPoint(p1, p2):
        x, y, R = p1
        a, b, S = p2
        d = math.sqrt((abs(a - x)) ** 2 + (abs(b - y)) ** 2)
        if d > (R + S) or d < (abs(R - S)):
            # print("Two circles have no intersection")
            return []
        elif d == 0 and R == S:
            # print("Two circles have same center!")
            return []
        else:
            A = (R ** 2 - S ** 2 + d ** 2) / (2 * d)
            h = math.sqrt(R ** 2 - A ** 2)
            x2 = x + A * (a - x) / d
            y2 = y + A * (b - y) / d
            x3 = x2 - h * (b - y) / d
            y3 = y2 + h * (a - x) / d
            x4 = x2 + h * (b - y) / d
            y4 = y2 - h * (a - x) / d
            return [x3, y3, x4, y4]


class Solution:
    def antPass(self, geometry: List[List[int]], path: List[List[int]]) -> List[bool]:
        n = len(geometry)
        adj = [[] for _ in range(n)]

        for i in range(n):
            for j in range(i + 1, n):
                a = geometry[i]
                b = geometry[j]

                if len(a) == 4 and len(b) == 4:
                    res = GeometryUtil.TwoLinesCrossPoint(a, b, onLine=True)
                elif len(a) == 4 and len(b) == 3:
                    res = GeometryUtil.LineIntersectCircle(b, a)
                elif len(a) == 3 and len(b) == 4:
                    res = GeometryUtil.LineIntersectCircle(a, b)
                else:
                    res = GeometryUtil.TwoCirclesCrossPoint(a, b)
                if res:
                    adj[i].append(j)
                    adj[j].append(i)

        # print(adj)

        def check(a, b):
            visited = set()

            def dfs(x):
                if x == b:
                    return True
                visited.add(x)
                for y in adj[x]:
                    if y in visited: continue
                    if dfs(y): return True
                return False

            return dfs(a)

        ans = []
        for a, b in path:
            ans.append(check(a, b))
        return ans


true, false, null = True, False, None
cases = [
    # ([[2, 5, 7, 3], [1, 1, 4, 2], [4, 3, 2]], [[0, 1], [1, 2], [0, 2]], [true, true, true]),
    # ([[4, 1, 1], [3, 2, 1], [1, 4, 5, 4]], [[0, 1], [2, 0]], [true, false]),
    ([[5, 6, 5, 8], [4, 3, 6, 4], [2, 6, 5, 6], [0, 5, 0, 6], [4, 0, 6, 0]], [[2, 0], [2, 4]], [true, false]),
    ([[3, 2, 6, 2], [9, 0, 10, 0], [3, 0, 6, 0], [7, 2, 9, 3], [4, 1, 5, 2]], [[0, 1], [3, 4], [0, 3]],
     [false, false, false])
]

import aatest_helper

aatest_helper.run_test_cases(Solution().antPass, cases)

if __name__ == '__main__':
    pass
