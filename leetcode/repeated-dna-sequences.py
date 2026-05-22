#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        from collections import Counter
        his = Counter()
        ans = []
        for i in range(len(s) - 9):
            ss = s[i:i + 10]
            his[ss] += 1
            if his[ss] == 2:
                ans.append(ss)

        return ans
