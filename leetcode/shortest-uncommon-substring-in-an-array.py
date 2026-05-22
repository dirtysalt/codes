#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def shortestSubstrings(self, arr: List[str]) -> List[str]:
        def buildss(s, sz):
            res = []
            for i in range(len(s) - sz + 1):
                res.append(s[i:i + sz])
            return res

        def buildss2(s):
            res = []
            for sz in range(1, len(s) + 1):
                res.extend(buildss(s, sz))
            return res

        from collections import defaultdict
        index = defaultdict(set)
        for i in range(len(arr)):
            res = buildss2(arr[i])
            for r in res:
                index[r].add(i)

        ans = [""] * len(arr)
        for i in range(len(arr)):
            s = arr[i]
            for sz in range(1, len(s) + 1):
                pot = []
                res = buildss(s, sz)
                for r in res:
                    if len(index[r]) == 1:
                        pot.append(r)
                if pot:
                    ans[i] = min(pot)
                    break
        return ans


if __name__ == '__main__':
    pass
