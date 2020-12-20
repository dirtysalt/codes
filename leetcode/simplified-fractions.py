#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def simplifiedFractions(self, n: int) -> List[str]:
        def gcd(a, b):
            while b != 0:
                a, b = b, a % b
            return a

        def reduce(a, b):
            g = gcd(a, b)
            return a // g, b // g

        ans = set()
        for x in range(1, n + 1):
            for y in range(1, x):
                a, b = reduce(y, x)
                ans.add((a, b))
        ans = sorted(ans)
        ans = ['%d/%d' % (x, y) for (x, y) in ans]
        return ans


cases = [
    (4, ["1/2", "1/3", "1/4", "2/3", "3/4"]),
    (3, ["1/2", "1/3", "2/3"])
]
import aatest_helper

aatest_helper.run_test_cases(Solution().simplifiedFractions, cases)
