#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def magicalString(self, n: int) -> int:
        tmp = [1, 2, 2]
        idx = 2
        while len(tmp) < n:
            x = tmp[idx]
            value = (2 - tmp[-1]) + 1
            for _ in range(x):
                tmp.append(value)
            idx += 1
        # print(tmp)
        ans = 0
        for i in range(n):
            if tmp[i] == 1:
                ans += 1
        return ans


cases = [
    (6, 3),
    (20, 10)
]

import aatest_helper

aatest_helper.run_test_cases(Solution().magicalString, cases)
