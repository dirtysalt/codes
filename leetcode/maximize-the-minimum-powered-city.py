#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def maxPower(self, stations: List[int], r: int, k: int) -> int:

        def test(M, K):
            n = len(stations)
            acc = [0] * (n + 1)
            for i in range(n):
                acc[i + 1] = acc[i] + stations[i]

            for i in range(n):
                begin = max(i - r, 0)
                end = min(i + r + 1, n)
                # end maybe has been updated.
                if end <= n:
                    acc[end] = max(acc[end], acc[end - 1] + stations[end - 1])
                a = acc[begin]
                b = acc[end]
                if b - a < M:
                    extra = M + a - b
                    if extra > K: return False
                    K -= extra
                    acc[end] += extra
            return True

        INF = k + sum(stations)
        s, e = 0, INF
        while s <= e:
            m = (s + e) // 2
            if test(m, k):
                s = m + 1
            else:
                e = m - 1
        ans = e
        return ans


class Solution:
    def maxPower(self, stations: List[int], r: int, k: int) -> int:
        n = len(stations)
        acc = [0] * (n + 1)
        for i in range(n):
            acc[i + 1] = acc[i] + stations[i]

        def test(M, K):
            diff = [0] * (n + 1)
            DIFF = 0
            for i in range(n):
                begin = max(i - r, 0)
                end = min(i + r + 1, n)
                DIFF += diff[i]
                SUM = acc[end] - acc[begin] + DIFF
                if SUM < M:
                    extra = M - SUM
                    if extra > K: return False
                    K -= extra
                    DIFF += extra
                    diff[min(i + r + 1 + r, n)] -= extra
            return True

        INF = k + sum(stations)
        s, e = 0, INF
        while s <= e:
            m = (s + e) // 2
            if test(m, k):
                s = m + 1
            else:
                e = m - 1
        ans = e
        return ans


true, false, null = True, False, None
import aatest_helper

cases = [
    ([1, 2, 4, 5, 0], 1, 2, 5),
    ([4, 4, 4, 4], 0, 3, 4),
    ([2, 10, 12, 3], 0, 14, 9),
    ([4, 2], 1, 1, 7,),
    ([13, 12, 8, 14, 7], 2, 23, 52)
]

aatest_helper.run_test_cases(Solution().maxPower, cases)

if __name__ == '__main__':
    pass
