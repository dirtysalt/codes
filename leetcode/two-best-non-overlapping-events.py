#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


# class Solution:
#     def maxTwoEvents(self, events: List[List[int]]) -> int:
#         events = [tuple(x) for x in events]
#         events.sort(key=lambda x: x[1])
#         st = [(0, 0)]
#         print(events)
#         for (s, e, v) in events:
#             lo, hi = 0, len(st) - 1
#             while lo <= hi:
#                 m = (lo + hi) // 2
#                 if st[m][0] < s:
#                     lo = m + 1
#                 else:
#                     hi = m - 1
#
#             v += st[hi][1]
#             if st[-1][0] == e:
#                 st[-1] = (e, max(v, st[-1][1]))
#             else:
#                 st.append((e, v))
#             print(st)
#
#         return max((x[1] for x in st))
#

class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        events = [tuple(x) for x in events]
        events.sort(key=lambda x: x[1])
        st = [(0, 0)]
        ans = 0
        for (s, e, v) in events:
            lo, hi = 0, len(st) - 1
            while lo <= hi:
                m = (lo + hi) // 2
                if st[m][0] < s:
                    lo = m + 1
                else:
                    hi = m - 1
            ans = max(ans, v + st[hi][1])

            if st[-1][0] == e:
                st[-1] = (e, max(v, st[-1][1]))
            elif v > st[-1][1]:
                st.append((e, v))

        return ans


true, false, null = True, False, None
cases = [
    ([[1, 3, 2], [4, 5, 2], [2, 4, 3]], 4),
    ([[1, 3, 2], [4, 5, 2], [1, 5, 5]], 5),
    ([[1, 5, 3], [1, 5, 1], [6, 6, 5]], 8),
    ([[10, 83, 53], [63, 87, 45], [97, 100, 32], [51, 61, 16]], 85),
]

import aatest_helper

aatest_helper.run_test_cases(Solution().maxTwoEvents, cases)

if __name__ == '__main__':
    pass
