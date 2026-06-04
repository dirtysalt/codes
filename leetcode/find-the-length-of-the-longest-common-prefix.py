#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        def get_prefix(a):
            a = str(a)
            res = set()
            for sz in range(1, len(a) + 1):
                res.add(a[:sz])
            return res

        A, B = set(), set()
        for a in arr1:
            A.update(get_prefix(a))
        for b in arr2:
            B.update(get_prefix(b))

        # print(A, B)
        C = A & B
        return max((len(x) for x in C)) if C else 0


if __name__ == '__main__':
    pass
