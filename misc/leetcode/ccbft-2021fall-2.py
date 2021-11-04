#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def analysisHistogram(self, heights: List[int], cnt: int) -> List[int]:
        heights.sort()

        ans = 1 << 30
        index = -1
        for i in range(len(heights) - cnt + 1):
            a = heights[i]
            b = heights[i + cnt - 1]
            diff = b - a
            if diff < ans:
                ans = diff
                index = i

        return heights[index: index + cnt]


if __name__ == '__main__':
    pass
