#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt
import functools


def F(s):
    @functools.cache
    def search(i, last, isLimit, isFirst):
        if i == len(s):
            return 0 if isFirst else 1

        ans = 0
        h = int(s[i])
        if isFirst:
            h2 = 9 if isLimit else h
            for d in range(0, h2 + 1):
                ans += search(i + 1, d, isLimit or d < h, d == 0)
        else:
            for d in (last - 1, last + 1):
                if d < 0 or d > 9 or (not isLimit and d > h): continue
                ans += search(i + 1, d, isLimit or d < h, False)
        return ans

    return search(0, 0, False, True)


def check(s):
    for i in range(1, len(s)):
        d = ord(s[i]) - ord(s[i - 1])
        if not (d == 1 or d == -1):
            return False
    return True


class Solution:
    def countSteppingNumbers(self, low: str, high: str) -> int:
        MOD = 10 ** 9 + 7
        h = F(high)
        l = F(low)
        ans = h - l
        if check(low):
            ans += 1
        return ans % MOD


true, false, null = True, False, None
import aatest_helper

cases = [
    ("1", "11", 10),
    ("90", "101", 2),
    ("23", "99", 14),
]

aatest_helper.run_test_cases(Solution().countSteppingNumbers, cases)

if __name__ == '__main__':
    pass
