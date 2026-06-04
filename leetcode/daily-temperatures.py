#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List

class Solution0:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        n = len(T)
        ans = [0] * n
        m = max(T)
        inf = 1 << 20
        his = [inf] * (m+1)

        for i in reversed(range(n)):
            x = T[i]
            if x != m:
                p = min(his[x + 1:])
                if p != inf:
                    ans[i] = p - i
            his[x] = i
        return ans

class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        n = len(T)
        st = []
        ans = [0] * n
        for i in reversed(range(n)):
            x = T[i]

            s, e = 0, len(st) - 1
            while s <= e:
                m = (s + e) // 2
                if st[m][0] > x:
                    s = m + 1
                else:
                    e = m - 1

            if 0 <= e < len(st):
                p = st[e][1]
                # print("t[{}]={}, st={}, p={}".format(i, x, st, p))
                ans[i] = p - i

            while st and st[-1][0] < x:
                st.pop()
            st.append((x, i))
        return ans

cases = [
    ([73, 74, 75, 71, 69, 72, 76, 73], [1, 1, 4, 2, 1, 1, 0, 0]),
    ([89, 62, 70, 58, 47, 47, 46, 76, 100, 70], [8, 1, 5, 4, 3, 2, 1, 1, 0, 0])
]

import aatest_helper

aatest_helper.run_test_cases(Solution().dailyTemperatures, cases)
