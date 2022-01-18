#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def maxRunTime(self, n: int, batteries: List[int]) -> int:
        batteries.sort(reverse=True)

        def check(k):
            tt = 0
            for x in batteries:
                tt += min(x, k)
            return tt >= n * k

        s, e = 0, sum(batteries)
        while s <= e:
            m = (s + e) // 2
            if check(m):
                s = m + 1
            else:
                e = m - 1
        return e

#
# class Solution:
#     def maxRunTime(self, n: int, batteries: List[int]) -> int:
#         batteries.sort(reverse=True)
#
#         tt = sum(batteries)
#         avg = 0
#         for x in batteries:
#             avg = tt // n
#             if x > avg:
#                 n -= 1
#                 tt -= x
#             else:
#                 break
#
#         return avg


if __name__ == '__main__':
    pass
