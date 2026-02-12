#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def minimumMoney(self, transactions: List[List[int]]) -> int:
        a, b = [], []
        for x, y in transactions:
            t = (x, y)
            if x > y:
                a.append(t)
            else:
                b.append(t)

        # 输出最低，输入最高
        a.sort(key=lambda x: (x[1], -x[0]))

        # 输入最高，输出最低
        b.sort(key=lambda x: (-x[0], x[1]))

        c = a + b
        ans = 0
        remain = 0
        for x, y in c:
            if remain < x:
                ans += (x - remain)
                remain = x
            remain -= x
            remain += y
        return ans


true, false, null = True, False, None
cases = [
    ([[2, 1], [5, 0], [4, 2]], 10),
    ([[3, 0], [0, 3]], 3),
    ([[3, 9], [0, 4], [7, 10], [3, 5], [0, 9], [9, 3], [7, 4], [0, 0], [3, 3], [8, 0]], 24),
]

import aatest_helper

aatest_helper.run_test_cases(Solution().minimumMoney, cases)

if __name__ == '__main__':
    pass
