#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        ss = text.split()
        ans = []
        for i in range(1, len(ss) - 1):
            if ss[i - 1] == first and ss[i] == second:
                ans.append(ss[i + 1])
        return ans
