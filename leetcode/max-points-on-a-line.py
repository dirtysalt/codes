#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt


class Solution:
    """
    @param points: an array of point
    @return: An integer
    """

    def maxPoints(self, points):
        # write your code here

        from collections import Counter, defaultdict
        cnt = Counter()
        for p in points:
            cnt[tuple(p)] += 1

        ps = list(cnt.keys())
        n = len(ps)
        if n == 0:
            return 0
        elif n == 1:
            return cnt[ps[0]]

        def norm(x, y):
            m = gcd(x, y)
            return x // m, y // m

        def gcd(a, b):
            while b != 0:
                a, b = b, a % b
            return a

        slope = defaultdict(set)
        for i in range(n):
            for j in range(i + 1, n):
                x = ps[i][0] - ps[j][0]
                y = ps[i][1] - ps[j][1]
                if x == 0:
                    ft = (1, 1 << 30, 1, ps[i][0])
                elif y == 0:
                    ft = (1, 0, 1, ps[i][1])
                else:
                    a, b = slp = norm(x, y)
                    cut = norm(ps[i][1] * a - ps[i][0] * b, b)
                    ft = (slp, cut)
                slope[ft].add(i)
                slope[ft].add(j)

        ans = 0
        for ft, xs in slope.items():
            res = 0
            for x in xs:
                res += cnt[ps[x]]
            ans = max(ans, res)
        return ans


cases = [
    ([[-435, -347], [-435, -347], [609, 613], [-348, -267], [-174, -107], [87, 133], [-87, -27], [-609, -507],
      [435, 453], [-870, -747], [-783, -667], [0, 53], [-174, -107], [783, 773], [-261, -187], [-609, -507],
      [-261, -187], [-87, -27], [87, 133], [783, 773], [-783, -667], [-609, -507], [-435, -347], [783, 773],
      [-870, -747], [87, 133], [87, 133], [870, 853], [696, 693], [0, 53], [174, 213], [-783, -667], [-609, -507],
      [261, 293], [435, 453], [261, 293], [435, 453]], 37),
    ([[0, -12], [5, 2], [2, 5], [0, -5], [1, 5], [2, -2], [5, -4], [3, 4], [-2, 4], [-1, 4], [0, -5], [0, -8],
      [-2, -1], [0, -11], [0, -9]], 6),
    ([[0, 0], [94911151, 94911150], [94911152, 94911151]], 2),
]

import aatest_helper

aatest_helper.run_test_cases(Solution().maxPoints, cases)
