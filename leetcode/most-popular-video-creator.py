#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def mostPopularCreator(self, creators: List[str], ids: List[str], views: List[int]) -> List[List[str]]:
        from collections import Counter
        cc = Counter()
        for c, v in zip(creators, views):
            cc[c] += v

        popular = max(cc.values())
        cs = set()
        for c, v in cc.items():
            if v == popular:
                cs.add(c)

        ss = []
        for c, id, v in zip(creators, ids, views):
            if c in cs:
                ss.append((c, -v, id))
        ss.sort()

        ans = []
        for c, v, id in ss:
            if c in cs:
                ans.append((c, id))
                cs.remove(c)
        return ans


if __name__ == '__main__':
    pass
