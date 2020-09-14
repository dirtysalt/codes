#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


# 这里有个规律是，his里面的value肯定是以-1,-2,-3,-4这样连续存放的，
# 所以其实不用二分直接hashmap去get就好了，如果找不到的话，通常意味着这是一个更小的值
# class Solution:
#     def longestWPI(self, hours: List[int]) -> int:
#         ans = 0
#         acc = 0
#         his = []
#
#         # def find_pos(x):
#         #     res = [idx for (y, idx) in his if y <= x]
#         #     if not res:
#         #         return None
#         #     return min(res)
#
#         def find_pos(x):
#             s, e = 0, len(his) - 1
#             while s <= e:
#                 m = (s + e) // 2
#                 if his[m][0] > x:
#                     s = m + 1
#                 else:
#                     e = m - 1
#             if s == len(his):
#                 return None
#             return his[s][1]
#
#         for i in range(len(hours)):
#             if hours[i] > 8:
#                 acc += 1
#             else:
#                 acc -= 1
#
#             # if acc < 1, it has to subtract least (acc-1)
#             # find first position where <= (acc-1)
#             if acc < 1:
#                 j = find_pos(acc - 1)
#                 if j is None:
#                     j = i
#             else:
#                 j = -1
#
#             if not his or his[-1][0] > acc:
#                 his.append((acc, i))
#             ans = max(ans, i - j)
#
#         return ans

class Solution:
    def longestWPI(self, hours: List[int]) -> int:
        ans = 0
        acc = 0
        his = {}

        for i in range(len(hours)):
            if hours[i] > 8:
                acc += 1
            else:
                acc -= 1

            # if acc < 1, it has to subtract least (acc-1)
            # find first position where <= (acc-1)
            if acc < 1:
                j = his.get(acc - 1)
                if j is None:
                    if acc not in his:
                        his[acc] = i
                    j = i
            else:
                j = -1
            ans = max(ans, i - j)

        return ans


cases = [
    ([6, 6, 6, 6, ], 0),
    ([6, 9, 9], 3),
    ([6, 6, 6, 9], 1),
    ([9, 9, 6, 0, 6, 6, 9], 3)
]
import aatest_helper

aatest_helper.run_test_cases(Solution().longestWPI, cases)
