#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def computeSimilarities(self, docs: List[List[int]]) -> List[str]:
        docs2 = [set(x) for x in docs]
        n = len(docs2)
        ans = []
        for i in range(n):
            for j in range(i + 1, n):
                a = len(docs2[i] & docs2[j])
                if a == 0: continue
                b = len(docs2[i] | docs2[j])
                ans.append((a / b + 1e-9, i, j))

        ans.sort(reverse=True)
        ans = ['%d,%d: %.4f' % (i, j, r) for (r, i, j) in ans]
        return ans
