#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def constructDistancedSequence(self, n: int) -> List[int]:
        ans = [0] * (2 * n - 1)
        mask = [0] * (n + 1)

        def dfs(p, filled):
            if filled == n: return True
            while p < len(ans) and ans[p] != 0: p += 1
            for x in reversed(range(1, n + 1)):
                if mask[x]: continue
                ans[p] = x
                mask[x] = 1

                if x != 1:
                    p2 = p + x
                    if p2 < len(ans) and ans[p2] == 0:
                        ans[p2] = x
                        if dfs(p + 1, filled + 1):
                            return True
                        ans[p2] = 0
                else:
                    if dfs(p + 1, filled + 1):
                        return True

                ans[p] = 0
                mask[x] = 0
            return False

        dfs(0, 0)
        # print(ans)
        return ans


import aatest_helper

cases = [
    (3, [3, 1, 2, 3, 2]),
    (5, [5, 3, 1, 4, 3, 5, 2, 4, 2]),
    (20, aatest_helper.ANYTHING)
]

aatest_helper.run_test_cases(Solution().constructDistancedSequence, cases)
