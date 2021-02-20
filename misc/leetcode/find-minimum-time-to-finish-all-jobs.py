#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def minimumTimeRequired(self, jobs: List[int], k: int) -> int:
        jobs.sort(reverse=True)
        n = len(jobs)
        Values = [0] * (1 << n)
        for st in range(1 << n):
            c = 0
            for i in range(n):
                if (st >> i) & 0x1:
                    c += jobs[i]
            Values[st] = c

        def QuickTest(T):
            n = len(jobs)
            mask = [0] * n
            for _ in range(k):
                t = 0
                for i in range(n):
                    if mask[i]: continue
                    if t + jobs[i] > T: continue
                    t += jobs[i]
                    mask[i] = 1
            for i in range(n):
                if mask[i] == 0: return False
            return True

        def test(T):
            # print(T)
            if QuickTest(T): return True

            import functools
            @functools.lru_cache(maxsize=None)
            def search(st, k, T):
                if k == 1: return Values[st] <= T
                st2 = st
                while st2:
                    if Values[st2] <= T:
                        if search(st & ~st2, k - 1, T):
                            return True
                    st2 = (st2 - 1) & st
                return False

            if search((1 << n) - 1, k, T):
                return True
            return False

        s, e = 0, sum(jobs)
        while s <= e:
            m = (s + e) // 2
            if test(m):
                e = m - 1
            else:
                s = m + 1
        ans = s
        return ans


cases = [
    ([3, 2, 3], 3, 3),
    ([1, 2, 4, 7, 8], 2, 11),
    ([6518448, 8819833, 7991995, 7454298, 2087579, 380625, 4031400, 2905811, 4901241, 8480231, 7750692, 3544254], 4,
     16274131),
    ([254, 256, 256, 254, 251, 256, 254, 253, 255, 251, 251, 255], 10, 504)
]

import aatest_helper

aatest_helper.run_test_cases(Solution().minimumTimeRequired, cases)
