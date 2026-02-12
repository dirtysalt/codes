#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


#
# class Solution:
#     def maxValue(self, events: List[List[int]], k: int) -> int:
#         n = len(events)
#         events.sort(key=lambda x: x[1])
#
#         import functools
#         @functools.lru_cache(maxsize=None)
#         def test(i, k, last):
#             if i == n: return 0
#             if k == 0: return 0
#             # O(n * k) <= 10^6.
#             ans = test(i + 1, k, last)
#             if events[i][0] > last:
#                 ans = max(ans, test(i + 1, k - 1, events[i][1]) + events[i][2])
#             return ans
#
#         ans = test(0, k, 0)
#         return ans


class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        n = len(events)
        events.sort(key=lambda x: x[0])

        import functools
        @functools.lru_cache(maxsize=None)
        def test(i, k):
            if i == n: return 0
            if k == 0: return 0
            # O(n * k) <= 10^6.
            ans = test(i + 1, k)
            # if taken, search next possible meeting.
            end = events[i][1]
            s, e = i + 1, n - 1
            while s <= e:
                m = (s + e) // 2
                if events[m][0] <= end:
                    s = m + 1
                else:
                    e = m - 1
            ans = max(ans, test(s, k - 1) + events[i][2])
            return ans

        ans = test(0, k)
        return ans


cases = [
    ([[1, 2, 4], [3, 4, 3], [2, 3, 1]], 2, 7),
    ([[1, 2, 4], [3, 4, 3], [2, 3, 10]], 2, 10),
    ([[1, 1, 1], [2, 2, 2], [3, 3, 3], [4, 4, 4]], 3, 9)
]

import aatest_helper

aatest_helper.run_test_cases(Solution().maxValue, cases)
