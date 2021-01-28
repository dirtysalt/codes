#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


# 另外一种办法是将它转成largest rectangle in histogram.
# https://leetcode.com/problems/maximal-rectangle/discuss/165472/Largest-Rectangle-Python

class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0
        n, m = len(matrix), len(matrix[0])
        height = [0] * m
        ans = 0
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == '1':
                    height[j] += 1
                else:
                    height[j] = 0

            # print(i, height)
            st = []
            for j in range(m):
                h = height[j]
                k = j
                while st and h <= st[-1][0]:
                    (h2, k2) = st.pop()
                    area = h2 * (j - k2)
                    ans = max(ans, area)
                    k = k2
                if h != 0:
                    st.append((h, k))
            while st:
                (h, k) = st.pop()
                area = h * (m - k)
                ans = max(ans, area)
        return ans
