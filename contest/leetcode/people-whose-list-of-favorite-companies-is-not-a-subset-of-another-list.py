#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def peopleIndexes(self, favoriteCompanies: List[List[str]]) -> List[int]:
        index = {}
        for xs in favoriteCompanies:
            for x in xs:
                if x not in index:
                    index[x] = len(index)

        fcs = []
        for xs in favoriteCompanies:
            tmp = []
            for x in xs:
                tmp.append(index[x])
            fcs.append(set(tmp))

        ans = []
        for i in range(len(fcs)):
            ok = True
            for j in range(len(fcs)):
                if i == j: continue
                # print(fcs[i], fcs[j])
                if len(fcs[i]) > len(fcs[j]): continue
                if fcs[i].issubset(fcs[j]):
                    ok = False
                    break
            if ok:
                ans.append(i)
        return ans
