#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def threeEqualParts(self, arr: List[int]) -> List[int]:
        n = len(arr)
        acc = [0] * (n + 1)
        for i in range(n):
            acc[i + 1] = (acc[i] << 1) | arr[i]

        def get_value(i, j):
            res = acc[j + 1] - (acc[i] << (j - i + 1))
            return res

        for i in range(n - 2):
            x = get_value(0, i)

            s, e = i + 1, n - 2
            while s <= e:
                m = (s + e) // 2
                value = get_value(i + 1, m)
                if value < x:
                    s = m + 1
                else:
                    e = m - 1

            if s == n - 1: continue
            v2 = get_value(i + 1, s)
            v3 = get_value(s + 1, n - 1)
            # print(i, s, x, v2, v3)
            if x == v2 == v3:
                return [i, s + 1]
        return [-1, -1]


class Solution:
    def threeEqualParts(self, arr: List[int]) -> List[int]:
        t = sum(arr)
        n = len(arr)
        if t % 3 != 0: return [-1, -1]
        if t == 0: return [0, 2]

        t = t // 3
        pos = -1
        for i in reversed(range(n)):
            if arr[i] == 1:
                t -= 1
                if t == 0:
                    pos = i
                    break

        p = arr[pos:]
        # P 0000  P 00000 P
        # P  a    P  b    P
        # ^       ^
        ans = []

        # search first pattern
        arr = arr[:pos]
        a = arr.index(1)
        if arr[a:a + len(p)] != p:
            return [-1, -1]
        ans.append(a + len(p) - 1)

        # search second pattern
        # but we cut of first part + 1
        # so later we have to add back ans[0] + 1
        arr = arr[a + len(p):]
        a = arr.index(1)

        if arr[a:a + len(p)] != p:
            return [-1, -1]
        ans.append(a + len(p))

        # all zeros
        arr = arr[a + len(p):]
        if arr and sum(arr) != 0:
            return [-1, -1]

        ans[1] += ans[0] + 1
        return ans


true, false, null = True, False, None
cases = [
    ([1, 0, 1, 0, 1], [0, 3]),
    ([1, 1, 0, 1, 1], [-1, -1]),
    ([1, 1, 0, 0, 1], [0, 2]),
    ([0, 0, 0], [0, 2])
]

import aatest_helper

aatest_helper.run_test_cases(Solution().threeEqualParts, cases)

if __name__ == '__main__':
    pass
