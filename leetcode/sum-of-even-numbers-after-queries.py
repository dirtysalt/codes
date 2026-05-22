#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def sumEvenAfterQueries(self, A: List[int], queries: List[List[int]]) -> List[int]:
        ans = []
        acc = 0
        for x in A:
            if x % 2 == 0:
                acc += x

        for val, idx in queries:
            x = A[idx] + val
            if x % 2 == 0:
                acc += x
            if A[idx] % 2 == 0:
                acc -= A[idx]
            A[idx] = x
            ans.append(acc)
        return ans

