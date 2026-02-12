#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def maximumTastiness(self, price: List[int], k: int) -> int:
        price.sort()

        def test(X):
            i = 0
            r = 1
            for j in range(1, len(price)):
                if (price[j] - price[i]) >= X:
                    i = j
                    r += 1
            return r >= k

        s, e = 0, price[-1]
        while s <= e:
            m = (s + e) // 2
            if test(m):
                s = m + 1
            else:
                e = m - 1
        return e


true, false, null = True, False, None
import aatest_helper

cases = [
    ([13, 5, 1, 8, 21, 2], 3, 8),
    ([1, 3, 1], 2, 2),
    ([7, 7, 7, 7], 2, 0),
]

aatest_helper.run_test_cases(Solution().maximumTastiness, cases)

if __name__ == '__main__':
    pass
