#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import defaultdict
        g = defaultdict(list)

        for x in strs:
            ft = ''.join(sorted(x))
            g[ft].append(x)

        ans = []
        for v in g.values():
            ans.append(v)
        return ans
