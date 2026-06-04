#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        def parse(x):
            m, d = x.split('-')
            d = int(d)
            for i in range(int(m) - 1):
                d += days[i]
            return d

        a, b = parse(arriveAlice), parse(leaveAlice)
        c, d = parse(arriveBob), parse(leaveBob)
        # print(a, b, c, d)
        ans = 0
        for x in range(1, 366):
            if x >= a and x <= b and x >= c and x <= d:
                ans += 1
        return ans


if __name__ == '__main__':
    pass
