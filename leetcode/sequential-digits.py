#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        def get_numbers(n):
            for i in range(1, 10 - n + 1):
                res = 0
                j = i
                for _ in range(n):
                    res = res * 10 + j
                    j += 1
                yield res

        def bits10(x):
            res = 0
            while x:
                x = x // 10
                res += 1
            return res

        ans = []
        for i in range(bits10(low), bits10(high) + 1):
            for v in get_numbers(i):
                if low <= v <= high:
                    ans.append(v)
        return ans


cases = [
    (100, 300, [123, 234]),
    (1000, 13000, [1234, 2345, 3456, 4567, 5678, 6789, 12345]),
]

import aatest_helper

aatest_helper.run_test_cases(Solution().sequentialDigits, cases)
