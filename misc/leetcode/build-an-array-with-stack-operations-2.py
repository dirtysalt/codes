#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        p = 0
        ans = []
        for x in target:
            ans += ["Push", "Pop"] * (x - p)
            ans.pop()
            # ans += ["Push"] * (x - p)
            # ans += ["Pop"] * (x - p - 1)
            p = x
        return ans
