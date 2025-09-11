#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        ans = []
        j = 0
        for i in range(1, n + 1):
            x = target[j]
            if x != i:
                ans.append("Push")
                ans.append("Pop")
            else:
                ans.append("Push")
                j += 1
                if j == len(target):
                    break
        return ans
