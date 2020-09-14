#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def largeGroupPositions(self, S):
        """
        :type S: str
        :rtype: List[List[int]]
        """

        n = len(S)
        pos = 0
        ans = []
        for i in range(1, n):
            if S[i] == S[pos]:
                continue
            if (i - pos) >= 3:
                ans.append((pos, i - 1))
            pos = i
        if (n - pos) >= 3:
            ans.append((pos, n - 1))
        return ans
