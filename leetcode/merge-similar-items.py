#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
        d1 = dict(items1)
        d2 = dict(items2)
        for k, v in d2.items():
            if k not in d1:
                d1[k] = 0
            d1[k] += v

        keys = list(d1.keys())
        keys.sort()
        ans = []
        for k in keys:
            ans.append([k, d1[k]])
        return ans


if __name__ == '__main__':
    pass
