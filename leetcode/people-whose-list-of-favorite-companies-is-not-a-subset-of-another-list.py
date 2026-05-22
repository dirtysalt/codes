#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def peopleIndexes(self, favoriteCompanies: List[List[str]]) -> List[int]:
        from collections import defaultdict
        groups = defaultdict(set)

        for p, cs in enumerate(favoriteCompanies):
            for c in cs:
                groups[c].add(p)

        ans = []
        n = len(favoriteCompanies)
        for p, cs in enumerate(favoriteCompanies):
            common = set(range(n))
            for c in cs:
                common = common & groups[c]
                if len(common) == 1:
                    break
            if len(common) == 1:
                ans.append(p)
        return ans
