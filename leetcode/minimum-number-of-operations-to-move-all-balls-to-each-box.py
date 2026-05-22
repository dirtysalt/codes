#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        n = len(boxes)
        ans = [0] * n
        for i in range(n):
            for j in range(i + 1, n):
                if boxes[i] == '1':
                    ans[j] += (j - i)
                if boxes[j] == '1':
                    ans[i] += (j - i)
        return ans
