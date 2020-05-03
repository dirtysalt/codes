#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt
from typing import List

from leetcode.aatest_helper import run_test_cases


class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        houses.sort()
        heaters.sort()

        def ok_to_cover(r):
            i, j = 0, 0
            while i < len(houses):
                if houses[i] < (heaters[j] - r):
                    return False
                elif houses[i] > (heaters[j] + r):
                    j += 1
                    if j >= len(heaters):
                        return False
                else:
                    i += 1
            return True

        # def ok_to_cover(r):
        #     last = 0
        #     for i in range(len(heaters)):
        #         x, y = heaters[i] - r, heaters[i] + r
        #         li = bisect.bisect_left(houses, x, lo=last)
        #         if li > last:
        #             return False
        #         ri = bisect.bisect_right(houses, y)
        #         last = ri
        #     if last != len(houses):
        #         return False
        #     return True

        max_radius = max(heaters[-1] - houses[0], -(heaters[0] - houses[-1]))
        s, e, res = 0, max_radius, max_radius
        while s <= e:
            m = (s + e) // 2
            if ok_to_cover(m):
                res = min(res, m)
                e = m - 1
            else:
                s = m + 1
        return res


cases = [
    ([282475249, 622650073, 984943658, 144108930, 470211272, 101027544, 457850878, 458777923],
     [823564440, 115438165, 784484492, 74243042, 114807987, 137522503, 441282327, 16531729, 823378840, 143542612],
     161834419),
    ([1, 5], [2], 3),
    ([1, 2, 3], [2], 1),
    ([1, 2, 3, 4], [1, 4], 1),
    ([1, 5], [10], 9),
    ([1], [1, 2, 3, 4], 0),
    ([1, 2, 3, 5, 15], [2, 30], 13),

]

sol = Solution()
fn = sol.findRadius
run_test_cases(fn, cases)
