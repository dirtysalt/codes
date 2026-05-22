#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        n = len(colors)

        def check(i):
            for k2 in range(k - 1):
                if colors[(i + k2) % n] != 1 - colors[(i + k2 + 1) % n]:
                    return False, i + k2 + 1
            return True, i + 1

        ans = 0
        ok, i = check(0)
        if ok: ans += 1
        while i < n:
            if ok and colors[(i + k - 2) % n] == 1 - colors[(i + k - 1) % n]:
                ans += 1
                i += 1
            else:
                ok, i = check(i)
                if ok: ans += 1
        return ans


true, false, null = True, False, None
import aatest_helper

cases = [
    ([0, 1, 0, 0, 1, 0, 1], 6, 2),
]

aatest_helper.run_test_cases(Solution().numberOfAlternatingGroups, cases)

if __name__ == '__main__':
    pass
