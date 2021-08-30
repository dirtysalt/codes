#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def minSessions(self, tasks: List[int], sessionTime: int) -> int:
        n = len(tasks)

        import functools
        @functools.lru_cache(maxsize=None)
        def query(st, k, space):
            if st == 0:
                return k

            ans = (n + 1)
            choose = False
            for j in range(n):
                if (st >> j) & 0x1:
                    if space >= tasks[j]:
                        res = query(st & ~(1 << j), k, space - tasks[j])
                        ans = min(ans, res)
                        choose = True

            if not choose:
                res = query(st, k + 1, sessionTime)
                ans = min(ans, res)
            return ans

        ans = query((1 << n) - 1, 1, sessionTime)
        return ans


class Solution:
    def minSessions(self, tasks: List[int], sessionTime: int) -> int:
        n = len(tasks)

        valid = [0] * (1 << n)
        for st in range(1 << n):
            t = 0
            for i in range(n):
                if (st >> i) & 0x1:
                    t += tasks[i]
            if t <= sessionTime:
                valid[st] = 1

        # print(valid)
        dp = [-1] * (1 << n)
        dp[0] = 0
        for st in range(1, 1 << n):
            x = st
            res = n + 1
            while True:
                x = x & st
                if not x: break
                if valid[x]:
                    t = 1 + dp[st ^ x]
                    res = min(res, t)
                x = x - 1
            dp[st] = res

        ans = dp[-1]
        return ans


true, false, null = True, False, None
cases = [
    ([1, 2], 3, 1),
    ([1, 2, 3], 3, 2),
    ([3, 1, 3, 1, 1], 8, 2),
    ([1, 2, 3, 4, 5], 15, 1)
]

import aatest_helper

aatest_helper.run_test_cases(Solution().minSessions, cases)

if __name__ == '__main__':
    pass
