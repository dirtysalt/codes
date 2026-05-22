#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def maximumGood(self, statements: List[List[int]]) -> int:
        n = len(statements)

        ans = 0
        for st in range(1 << n):
            ok = True

            for i in range(n):
                xi = (st >> i) & 0x1
                if xi == 0: continue

                for j in range(n):
                    xj = (st >> j) & 0x1
                    x = statements[i][j]
                    if x == 2: continue
                    if x != xj:
                        ok = False
                        break

                if not ok:
                    break

            if ok:
                cnt = 0
                for i in range(n):
                    if st & (1 << i):
                        cnt += 1
                ans = max(ans, cnt)
        return ans


true, false, null = True, False, None
cases = [
    ([[2, 1, 2], [1, 2, 2], [2, 0, 2]], 2),
    ([[2, 0], [0, 2]], 1),
]

import aatest_helper

aatest_helper.run_test_cases(Solution().maximumGood, cases)

if __name__ == '__main__':
    pass
