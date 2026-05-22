#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def makeIntegerBeautiful(self, n: int, target: int) -> int:
        ss = []
        while n:
            ss.append(n % 10)
            n = n // 10

        def add(i, d):
            while i < len(ss):
                ss[i] += d
                if ss[i] >= 10:
                    ss[i] -= 10
                    i += 1
                    d = 1
                else:
                    return sum(ss)
            ss.append(d)
            return sum(ss)

        i = 0
        ans = 0
        now = sum(ss)
        while now > target:
            while i < len(ss) and ss[i] == 0: i += 1
            d = 10 - ss[i]
            ans += d * (10 ** i)
            now = add(i, d)
        return ans


true, false, null = True, False, None
cases = [
    (16, 6, 4),
    (467, 6, 33),
    (1, 1, 0),
]

import aatest_helper

aatest_helper.run_test_cases(Solution().makeIntegerBeautiful, cases)

if __name__ == '__main__':
    pass
