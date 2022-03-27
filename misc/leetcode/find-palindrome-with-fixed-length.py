#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def kthPalindrome(self, queries: List[int], intLength: int) -> List[int]:
        def test(k, length):
            res = []

            L = (length + 1) // 2
            k -= 1
            base = 10 ** (L - 1)
            if k >= 9 * base:
                return -1

            d = (k // base) + 1
            k %= base
            res.append(d)

            for _ in range(L - 1):
                base //= 10
                d = k // base
                k %= base
                res.append(d)

            if length % 2 == 0:
                res = res + res[::-1]
            else:
                res = res[:-1] + res[::-1]

            value = 0
            for x in res:
                value = value * 10 + x
            return value

        ans = []
        for q in queries:
            ans.append(test(q, intLength))
        return ans


true, false, null = True, False, None
cases = [
    ([1, 2, 3, 4, 5, 90], 3, [101, 111, 121, 131, 141, 999]),
    ([2, 4, 6], 4, [1111, 1331, 1551]),
]

import aatest_helper

aatest_helper.run_test_cases(Solution().kthPalindrome, cases)

if __name__ == '__main__':
    pass
