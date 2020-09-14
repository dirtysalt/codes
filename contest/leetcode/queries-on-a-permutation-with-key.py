#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def processQueries(self, queries: List[int], m: int) -> List[int]:
        A = list(range(m))
        ans = []
        for q in queries:
            idx = A.index(q - 1)
            ans.append(idx)
            A = [q - 1] + A[:idx] + A[idx + 1:]
        return ans
