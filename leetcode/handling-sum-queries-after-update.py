#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def handleQuery(self, nums1: List[int], nums2: List[int], queries: List[List[int]]) -> List[int]:
        s = sum(nums2)
        x = int(''.join(map(str, nums1[::-1])), 2)

        ans = []
        for op, l, r in queries:
            if op == 1:
                y = (1 << (r - l + 1)) - 1
                y <<= l
                x = x ^ y
            elif op == 2:
                s += l * x.bit_count()
            else:
                ans.append(s)

        return ans


class Solution:
    def handleQuery(self, nums1: List[int], nums2: List[int], queries: List[List[int]]) -> List[int]:
        n = len(nums1)
        cnt = [0] * (4 * n)
        lazy = [False] * (4 * n)

        def maintain(i):
            cnt[i] = cnt[2 * i] + cnt[2 * i + 1]

        def build(i, l, r):
            if l == r:
                cnt[i] = nums1[l - 1]
                return

            m = (l + r) // 2
            build(2 * i, l, m)
            build(2 * i + 1, m + 1, r)
            maintain(i)
            return

        def flip(i, l, r, L, R):
            def fix(i, l, r):
                cnt[i] = (r - l + 1) - cnt[i]
                lazy[i] = not lazy[i]
                return

            if l <= L and R <= r:
                fix(i, L, R)
                return

            M = (L + R) // 2
            if lazy[i]:
                lazy[i] = False
                fix(2 * i, L, M)
                fix(2 * i + 1, M + 1, R)
                maintain(i)

            if l <= M: flip(2 * i, l, r, L, M)
            if (M + 1) <= r: flip(2 * i + 1, l, r, M + 1, R)
            maintain(i)

        build(1, 1, n)
        ans, base = [], sum(nums2)
        for op, l, r in queries:
            if op == 1:
                flip(1, l + 1, r + 1, 1, n)
            elif op == 2:
                base += l * cnt[1]
            else:
                ans.append(base)
        return ans


true, false, null = True, False, None
import aatest_helper

cases = [
    ([1, 0, 1], [0, 0, 0], [[1, 1, 1], [2, 1, 0], [3, 0, 0]], [3]),
    ([1], [5], [[2, 0, 0], [3, 0, 0]], [5]),
    ([0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 1, 0, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1],
     [30, 46, 43, 34, 39, 16, 14, 41, 22, 11, 32, 2, 44, 12, 22, 36, 44, 49, 50, 10, 33, 7, 42],
     [[1, 15, 21], [3, 0, 0], [3, 0, 0], [2, 21, 0], [2, 13, 0], [3, 0, 0]], [679, 679, 1053]),
]

aatest_helper.run_test_cases(Solution().handleQuery, cases)

if __name__ == '__main__':
    pass
