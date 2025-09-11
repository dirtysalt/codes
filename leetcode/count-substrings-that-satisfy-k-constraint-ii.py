#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt
from typing import List


class Solution:
    def countKConstraintSubstrings(self, s: str, k: int, queries: List[List[int]]) -> List[int]:
        n = len(s)

        def build_end():
            a, b = n, n
            right = [n] * (n + 1)
            for i in reversed(range(n)):
                if s[i] == '0':
                    right[i] = a
                    a = i
                else:
                    right[i] = b
                    b = i
            a, b = n, n
            for i in range(n):
                if s[i] == '0':
                    a = i
                    break
            for i in range(n):
                if s[i] == '1':
                    b = i
                    break
            for _ in range(k):
                a = right[a]
                b = right[b]

            end = [-1] * n
            for i in range(n):
                end[i] = max(a, b)
                if s[i] == '0':
                    a = right[a]
                else:
                    b = right[b]
            return end

        end = build_end()

        def search(x):
            s, e = 0, n - 1
            while s <= e:
                m = (s + e) // 2
                if end[m] <= x:
                    s = m + 1
                else:
                    e = m - 1
            return e

        acc = [0] * (n + 1)
        for i in range(n):
            acc[i + 1] = acc[i] + (end[i] - i)

        # print(end)
        ans = []
        for a, b in queries:
            p = search(b + 1)
            r = 0
            # [a...p]
            # where end[p] <= (b+1)
            if p >= a:
                r += acc[p + 1] - acc[a]
            else:
                p = a - 1

            # [p + 1 .. end + 1]
            # [p + 2 .. end + 1]
            # [end + 1.. end + 1]
            sz = (b + 1 - p)
            r += (b - p) * sz - (sz - 1) * sz // 2
            ans.append(r)

        return ans


true, false, null = True, False, None
import aatest_helper

cases = [
    aatest_helper.OrderedDict(s="0001111", k=2, queries=[[0, 6]], res=[26]),
    aatest_helper.OrderedDict(s="010101", k=1, queries=[[0, 5], [1, 4], [2, 3]], res=[15, 9, 3]),
    ("000", 1, [[0, 0], [0, 1], [0, 2], [1, 1], [1, 2], [2, 2]], [1, 3, 6, 1, 3, 1]),
    ("000", 1, [[1, 1]], [1])
]
aatest_helper.run_test_cases(Solution().countKConstraintSubstrings, cases)

if __name__ == '__main__':
    pass
