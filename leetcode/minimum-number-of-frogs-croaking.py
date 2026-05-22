#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def minNumberOfFrogs(self, croakOfFrogs: str) -> int:
        mapping = {'c': 0, 'r': 1, 'o': 2, 'a': 3, 'k': 4}
        cfs = [mapping[c] for c in croakOfFrogs]

        ways = [0] * 5
        ans = 0
        for c in cfs:
            if ways[c] == 0:
                if c == 0:
                    ans += 1
                else:
                    return -1
                ways[c] = 1
            ways[c] -= 1
            ways[(c + 1) % 5] += 1
        for i in range(1, 5):
            if ways[i] != 0:
                return -1
        return ans
