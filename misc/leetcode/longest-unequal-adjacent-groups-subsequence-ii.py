#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt
import functools
from typing import List


class Solution:
    def getWordsInLongestSubsequence(self, n: int, words: List[str], groups: List[int]) -> List[str]:
        @functools.cache
        def near(i, j):
            if len(words[i]) != len(words[j]):
                return False
            c = 0
            for k in range(len(words[i])):
                if words[i][k] != words[j][k]:
                    c += 1
                    if c >= 2: return False
            return c == 1

        @functools.cache
        def maxdist(i):
            if i == n:
                return 0, -1
            ans, idx = 1, n
            if i == -1:
                ans, idx = 0, n
            for j in range(i + 1, n):
                if i == -1 or (groups[i] != groups[j] and near(i, j)):
                    c, _ = maxdist(j)
                    c += 1
                    if c > ans:
                        ans, idx = c, j
            return ans, idx

        d, p = maxdist(-1)
        pos = [p]
        while True:
            _, p = maxdist(pos[-1])
            if p == n: break
            pos.append(p)

        ans = []
        # print(pos)
        for p in pos:
            ans.append(words[p])
        return ans


if __name__ == '__main__':
    pass
