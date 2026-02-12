#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def bestClosingTime(self, customers: str) -> int:
        Y, N = 0, 0
        for c in customers:
            if c == 'Y':
                Y += 1
            else:
                N += 1

        ans = 1 << 30
        y, n = 0, 0
        time = 0
        for i in range(len(customers) + 1):
            cost = n + (Y - y)
            if cost < ans:
                ans = cost
                time = i

            if i != len(customers):
                c = customers[i]
                if c == 'Y':
                    y += 1
                else:
                    n += 1

        return time


true, false, null = True, False, None
import aatest_helper

cases = [
    ("YYNY", 2),
    ("NNNNN", 0),
    ("YYYY", 4),
]

aatest_helper.run_test_cases(Solution().bestClosingTime, cases)

if __name__ == '__main__':
    pass
