#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def printVertically(self, s: str) -> List[str]:
        ss = [x.strip() for x in s.split()]
        m = max([len(x) for x in ss])
        res = [[] for _ in range(m)]

        for s in ss:
            for i in range(len(s)):
                res[i].append(s[i])

            for i in range(len(s), m):
                res[i].append(' ')

        print(res)
        ans = [''.join(x).rstrip() for x in res]
        return ans
