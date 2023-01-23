#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    """
    @param point: a list of two-tuples
    @return: a boolean, denote whether the polygon is convex
    """

    def isConvex(self, point):
        # write your code here

        def cross_product(v0, v1):
            # print(v0, v1)
            return v0[0] * v1[1] - v0[1] * v1[0]

        def vector(a, b):
            return b[0] - a[0], b[1] - a[1]

        n = len(point)
        pos = None
        for i in range(n):
            a = point[(i - 1 + n) % n]
            b = point[i]
            c = point[(i + 1) % n]
            # 参考convex-hull.py 整个旋转过程中需要始终保持一个方向
            cp0 = cross_product(vector(a, b), vector(a, c))
            if cp0 == 0:
                continue
            if pos is None:
                pos = cp0 > 0
            elif pos != (cp0 > 0):
                return False
        return True


if __name__ == '__main__':
    s = Solution()
    ps = [[0, 11], [1, 1], [17, 0], [17, 1], [16, 13], [5, 19]]
    print(s.isConvex(ps))
    ps = [[0, 0], [0, 10], [10, 10], [10, 0], [5, 5]]
    print(s.isConvex(ps))
    ps = [[-495, 377], [-489, 489], [-350, 496], [347, 499], [479, 493], [491, 437], [498, 25], [497, -376],
          [496, -456], [443, -494], [249, -499], [79, -498], [-491, -489], [-496, -378], [-497, 263]]
    print(s.isConvex(ps))
