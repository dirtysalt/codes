#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def captureForts(self, forts: List[int]) -> int:
        n = len(forts)
        ps = []
        for i in range(n):
            if forts[i] != 0:
                ps.append((forts[i], i))

        ans = 0
        for i in range(len(ps)):
            if ps[i][0] == -1:
                if (i - 1) >= 0 and ps[i - 1][0] == 1:
                    r = (ps[i][1] - ps[i - 1][1] - 1)
                    ans = max(ans, r)
                if (i + 1) < len(ps) and ps[i + 1][0] == 1:
                    r = (ps[i + 1][1] - ps[i][1] - 1)
                    ans = max(ans, r)

        return ans


true, false, null = True, False, None
import aatest_helper

cases = [
    ([1, 0, 0, -1, 0, 0, 0, 0, 1], 4),
    ([0, 0, 1, -1], 0),
]

aatest_helper.run_test_cases(Solution().captureForts, cases)

if __name__ == '__main__':
    pass
