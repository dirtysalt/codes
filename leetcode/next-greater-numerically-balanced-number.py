#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def nextBeautifulNumber(self, n: int) -> int:
        def ok(x):
            cnt = [0] * 10
            while x:
                y = x % 10
                cnt[y] += 1
                if cnt[y] > y:
                    return False
                x = x // 10

            for i in range(1, 10):
                if cnt[i] != 0 and cnt[i] != i:
                    return False
            return True

        n += 1
        while not ok(n):
            n += 1

        return n


true, false, null = True, False, None
cases = [
    (1, 22),
    (1000, 1333),
    (3000, 3133)
]

import aatest_helper

aatest_helper.run_test_cases(Solution().nextBeautifulNumber, cases)

if __name__ == '__main__':
    pass
