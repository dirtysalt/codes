#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def convertTime(self, current: str, correct: str) -> int:
        def tom(s):
            ss = s.split(':')
            return int(ss[0]) * 60 + int(ss[1])

        a = tom(current)
        b = tom(correct)
        d = (b - a)
        ans = 0
        for x in (60, 15, 5, 1):
            ans += d // x
            d %= x
        return ans


if __name__ == '__main__':
    pass
