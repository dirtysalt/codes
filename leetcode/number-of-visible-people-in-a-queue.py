#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        st = []
        n = len(heights)
        ans = [0] * n

        for i in reversed(range(n)):
            h = heights[i]

            # print(i, h, st)
            s, e = 0, len(st) - 1
            while s <= e:
                m = (s + e) // 2
                if st[m] < h:
                    e = m - 1
                else:
                    s = m + 1

            dist = 0
            # use e as index.
            if st:
                dist = len(st) - max(e, 0)
            ans[i] = dist

            while st and h > st[-1]:
                st.pop()
            st.append(h)

        return ans


true, false, null = True, False, None
cases = [
    ([10, 6, 8, 5, 11, 9], [3, 1, 2, 1, 1, 0]),
    ([5, 1, 2, 3, 10], [4, 1, 1, 1, 0])
]

import aatest_helper

aatest_helper.run_test_cases(Solution().canSeePersonsCount, cases)

if __name__ == '__main__':
    pass
