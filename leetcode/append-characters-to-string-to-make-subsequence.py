#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        n, m = len(s), len(t)
        j = 0
        for i in range(n):
            if j < m and t[j] == s[i]:
                j += 1
        return m - j


if __name__ == '__main__':
    pass
