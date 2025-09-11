#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt


class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """

        st = []  # (idx, height)
        res = 0
        for i in range(len(heights)):
            h = heights[i]
            idx = i
            while st and h < st[-1][1]:
                out = (i - st[-1][0]) * st[-1][1]
                idx = st[-1][0]
                st.pop()
                res = max(res, out)
            st.append((idx, h))

        i = len(heights)
        while st:
            out = (i - st[-1][0]) * st[-1][1]
            res = max(res, out)
            st.pop()
        return res


if __name__ == '__main__':
    s = Solution()
    print(s.largestRectangleArea([2, 1, 5, 6, 2, 3]))
    print(s.largestRectangleArea([2, 1, 2]))
