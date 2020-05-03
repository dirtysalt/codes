#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if not intervals: return []
        intervals.sort(key=lambda x: x.start)
        # print_intervals(intervals)
        res = []
        start, end = intervals[0].start, intervals[0].end
        for i in range(1, len(intervals)):
            a, b = intervals[i].start, intervals[i].end
            assert (start <= a)
            if a <= end:
                end = max(end, b)
            else:
                res.append((start, end))
                start, end = a, b
        res.append((start, end))
        return [Interval(p[0], p[1]) for p in res]


# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e


def list_to_intervals(xs):
    return [Interval(x[0], x[1]) for x in xs]


def print_intervals(xs):
    print(', '.join(['[%d, %d]' % (x.start, x.end) for x in xs]))


if __name__ == '__main__':
    s = Solution()
    print_intervals(s.merge(list_to_intervals([[1, 3], [2, 6], [8, 10], [15, 18]])))
    print_intervals(s.merge(list_to_intervals([[1, 4], [0, 4]])))
