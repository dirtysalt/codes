#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def leftmostBuildingQueries(self, heights: List[int], queries: List[List[int]]) -> List[int]:
        qs = []
        for i, q in enumerate(queries):
            x, y = q
            if x > y:
                x, y = y, x
            qs.append((x, y, i))

        qs.sort(key=lambda x: x[1])
        ans = [-1] * len(qs)
        st = []

        def search(x, y):
            # 可以直接到y, y满足条件
            if x == y or heights[x] < heights[y]:
                return y
            value = heights[x] + 1
            s, e = 0, len(st) - 1
            while s <= e:
                m = (s + e) // 2
                if st[m][0] >= value:
                    s = m + 1
                else:
                    e = m - 1
            if e < 0:
                e = -1
            else:
                e = st[e][1]
            return e

        for i in reversed(range(len(heights))):
            h = heights[i]
            while st and h >= st[-1][0]:
                st.pop()
            st.append((h, i))

            while qs and qs[-1][1] == i:
                x, y, idx = qs[-1]
                r = search(x, y)
                ans[idx] = r
                qs.pop()
        return ans


true, false, null = True, False, None
import aatest_helper

cases = [
    aatest_helper.OrderedDict(heights=[6, 4, 8, 5, 2, 7], queries=[[0, 1], [0, 3], [2, 4], [3, 4], [2, 2]],
                              res=[2, 5, -1, 5, 2]),
    aatest_helper.OrderedDict(heights=[5, 3, 8, 2, 6, 1, 4, 6], queries=[[0, 7], [3, 5], [5, 2], [3, 0], [1, 6]],
                              res=[7, 6, -1, 4, 6]),
    # ([1, 2, 1, 2, 1, 2],
    #  [[0, 0], [0, 1], [0, 2], [0, 3], [0, 4], [0, 5], [1, 0], [1, 1], [1, 2], [1, 3], [1, 4], [1, 5], [2, 0], [2, 1],
    #   [2, 2], [2, 3], [2, 4], [2, 5], [3, 0], [3, 1], [3, 2], [3, 3], [3, 4], [3, 5], [4, 0], [4, 1], [4, 2], [4, 3],
    #   [4, 4], [4, 5], [5, 0], [5, 1], [5, 2], [5, 3], [5, 4], [5, 5]],
    #  [0, 1, 3, 3, 5, 5, 1, 1, -1, -1, -1, -1, 3, -1, 2, 3, 5, 5, 3, -1, 3, 3, -1, -1, 5, -1, 5, -1, 4, 5, 5, -1, 5, -1,
    #   5, 5]
    #  ),
    ([1, 2, 1, 2, 1, 2], [[0, 2]], [3]),
]

aatest_helper.run_test_cases(Solution().leftmostBuildingQueries, cases)

if __name__ == '__main__':
    pass
