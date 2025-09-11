#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        a, b = set(), set()
        ans = []
        c = 0
        for x, y in zip(A, B):
            if x == y:
                c += 1
            else:
                if x in b:
                    c += 1
                if y in a:
                    c += 1
            a.add(x)
            b.add(y)
            ans.append(c)
        return ans


if __name__ == '__main__':
    pass
