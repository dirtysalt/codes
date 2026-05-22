#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def print(self, height, filled):
        n = len(height)
        max_height = max(height)
        out = [[' '] * n for _ in range(max_height)]

        for i, x in enumerate(height):
            for j in range(x):
                out[max_height - 1 - j][i] = 'X'

        for (r0, r1, h0, h1) in filled:
            for r in range(r0, r1):
                for h in range(h0, h1):
                    out[max_height - 1 - h][r] = 'C'

        for x in out:
            print(''.join(x))

    def trap(self, height: List[int]) -> int:
        st = []
        ans = 0
        filled = []

        for i, x in enumerate(height):
            if st and st[-1][1] <= x:
                (j, y) = st.pop()
                while st and st[-1][1] <= x:
                    (k, z) = st.pop()
                    ans += (z - y) * (i - k - 1)
                    filled.append((k + 1, i, y, z))
                    j, y = k, z
                if st:
                    ans += (x - y) * (i - st[-1][0] - 1)
                    filled.append((st[-1][0] + 1, i, y, x))

            st.append((i, x))

        # self.print(height, filled)
        return ans


cases = [
    ([4, 2, 3], 1),
    ([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1], 6)
]
import aatest_helper

aatest_helper.run_test_cases(Solution().trap, cases)
