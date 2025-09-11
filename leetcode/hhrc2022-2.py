#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def longestESR(self, sales: List[int]) -> int:
        xs = [1 if x > 8 else -1 for x in sales]
        n = len(xs)
        pos = [-1] * (2 * n + 2)

        acc = 0
        for i in range(n):
            acc += xs[i]
            pos[(acc + n)] = i

        for i in reversed(range(2 * n + 1)):
            pos[i] = max(pos[i], pos[i + 1])

        ans = 0
        acc = 0
        for i in range(n):
            j = pos[(acc + 1 + n)]
            dist = (j - i + 1)
            ans = max(ans, dist)
            acc += xs[i]
        return ans


true, false, null = True, False, None
cases = [
    ([10, 2, 1, 4, 3, 9, 6, 9, 9], 5),
    ([5, 6, 7], 0),
]

import aatest_helper

aatest_helper.run_test_cases(Solution().longestESR, cases)

if __name__ == '__main__':
    pass
