#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    """
    @param intervals: the intervals
    @param rooms: the sum of rooms
    @param ask: the ask
    @return: true or false of each meeting
    """

    def meetingRoomIII(self, intervals, rooms, ask):
        # Write your code here.
        from collections import Counter
        cnt = Counter()
        for s, e in intervals:
            cnt[s] += 1
            cnt[e] -= 1

        ts = sorted(cnt.keys())
        rs = []
        acc = 0
        start = 0
        for t in ts:
            rs.append((start, t, acc))
            acc += cnt[t]
            start = t

        rs = [(x, y, t) for (x, y, t) in rs if t == rooms]
        ans = []

        def overlap(r, q):
            (x, y, t) = r
            (s, e) = q
            if x >= e or y <= s:
                return False
            return True

        for q in ask:
            s, e = 0, len(rs) - 1
            while s <= e:
                m = (s + e) // 2
                if rs[m][0] >= q[0]:
                    e = m - 1
                else:
                    s = m + 1
            # check e and e + 1 overlap with q
            opts = [e, e + 1]
            ok = True
            for i in opts:
                if 0 <= i < len(rs):
                    if overlap(rs[i], q):
                        ok = False
                        break
            ans.append(ok)
        return ans
