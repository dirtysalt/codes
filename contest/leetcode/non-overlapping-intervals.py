#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

# 这道题目和LIS非常类似，但是必须使用O(nlgn)的解法，否则没有办法通过

# Definition for an interval.
import functools
from bisect import bisect


def cmp(x, y):
    if x < y:
        return -1
    elif x > y:
        return 1
    return 0


class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

    def __str__(self):
        return '[{}, {}]'.format(self.start, self.end)


# class Solution:
#     def eraseOverlapIntervals(self, intervals):
#         """
#         :type intervals: List[Interval]
#         :rtype: int
#         """
#         intervals.sort(key=functools.cmp_to_key(lambda x, y: cmp(x.start, y.start) or cmp(x.end, y.end)))
#         dp = []
#         dp.append(1)
#         n = len(intervals)
#         for idx in range(1, n):
#             p = intervals[idx]
#             res = 1
#             for i in range(idx):
#                 p2 = intervals[i]
#                 # not overlap.
#                 if p2.start >= p.end or p2.end <= p.start:
#                     res = max(res, dp[i] + 1)
#             dp.append(res)
#
#         # print(dp)
#         res = len(intervals) - max(dp)
#         return res

class Solution:
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        intervals.sort(key=functools.cmp_to_key(lambda x, y: cmp(x.start, y.start) or cmp(x.end, y.end)))
        res = []
        for p in intervals:
            index = bisect(res, p.start)
            if index == len(res):
                res.append(p.end)
            else:
                res[index] = min(res[index], p.end)
        # print(res)
        return len(intervals) - len(res)


def list_to_intervals(xs):
    return [Interval(x[0], x[1]) for x in xs]


def print_intervals(xs):
    print(', '.join(['[%d, %d]' % (x.start, x.end) for x in xs]))


if __name__ == '__main__':
    s = Solution()
    print(s.eraseOverlapIntervals(list_to_intervals([[1, 2], [2, 3], [3, 4], [1, 3]])))
    print(s.eraseOverlapIntervals(list_to_intervals([[1, 2], [1, 2], [1, 2]])))
    print(s.eraseOverlapIntervals(list_to_intervals([[1, 2], [2, 3]])))
    print(s.eraseOverlapIntervals(list_to_intervals([[0, 2], [1, 3], [2, 4], [3, 5], [4, 6]])))
    print(s.eraseOverlapIntervals(list_to_intervals([[0, 2], [1, 3], [1, 3], [2, 4], [3, 5], [3, 5], [4, 6]])))
