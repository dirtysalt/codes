#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        back = [[] for _ in range(n)]
        for x, y in edges:
            back[y].append(x)

        def search(x, res):
            if x in res:
                return
            res.add(x)
            for y in back[x]:
                search(y, res)

        ans = []
        for i in range(n):
            res = set()
            search(i, res)
            res.remove(i)
            ans.append(sorted(res))
        return ans


if __name__ == '__main__':
    pass
