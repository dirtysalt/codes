#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

"""
Definition of Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""


class Solution:
    """
    @param intervals: an array of meeting time intervals
    @return: the minimum number of conference rooms required
    """

    def minMeetingRooms(self, intervals):
        # Write your code here
        from collections import Counter
        cnt = Counter()
        for t in intervals:
            s, e = t.start, t.end
            cnt[s] += 1
            cnt[e + 1] -= 1

        ts = sorted(cnt.keys())
        ans = 0
        room = 0
        for t in ts:
            room += cnt[t]
            ans = max(ans, room)
        return ans
