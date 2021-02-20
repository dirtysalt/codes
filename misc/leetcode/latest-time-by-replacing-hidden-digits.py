#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def maximumTime(self, time: str) -> str:
        h, m = time.split(':')
        hh = 23
        if h == '??':
            hh = 23
        elif h[0] == '?':
            x = int(h[1])
            if x >= 4:
                hh = 10 + x
            else:
                hh = 20 + x
        elif h[1] == '?':
            x = int(h[0])
            if x == 0:
                hh = 9
            elif x == 1:
                hh = 19
            else:
                hh = 23
        else:
            hh = int(h)

        mm = 59
        if m == '??':
            mm = 59
        elif m[0] == '?':
            x = int(m[1])
            mm = 50 + x
        elif m[1] == '?':
            x = int(m[0])
            mm = x * 10 + 9
        else:
            mm = int(m)

        ans = '%02d:%02d' % (hh, mm)
        return ans


cases = [
    ("2?:?0", "23:50"),
    ("0?:3?", '09:39'),
    ("1?:22", '19:22'),
    ('?0:15', '20:15'),
]

import aatest_helper

aatest_helper.run_test_cases(Solution().maximumTime, cases)
