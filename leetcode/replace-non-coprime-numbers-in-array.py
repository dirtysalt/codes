#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def replaceNonCoprimes(self, nums: List[int]) -> List[int]:
        ans = []

        def gcd(a, b):
            while b != 0:
                a, b = b, a % b
            return a

        def lcm(a, b, g):
            return (a * b) // g

        def check(xs):
            value = xs.pop()
            while xs:
                x = xs[-1]
                g = gcd(value, x)
                if g == 1:
                    break
                xs.pop()
                value = lcm(value, x, g)
            xs.append(value)

        value = nums[0]
        ans = []
        for x in nums[1:]:
            g = gcd(value, x)
            if g == 1:
                ans.append(value)
                check(ans)
                value = x
            else:
                value = lcm(value, x, g)

        ans.append(value)
        check(ans)
        return ans


true, false, null = True, False, None
cases = [
    ([6, 4, 3, 2, 7, 6, 2], [12, 7, 6]),
    ([2, 2, 1, 1, 3, 3, 3], [2, 1, 1, 3]),
    ([287, 41, 49, 287, 899, 23, 23, 20677, 5, 825], [2009, 20677, 825]),
]

import aatest_helper

aatest_helper.run_test_cases(Solution().replaceNonCoprimes, cases)

if __name__ == '__main__':
    pass
