#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from collections import Counter


class Solution:
    def findValidPair(self, s: str) -> str:
        cnt = Counter(s)
        for i in range(len(s) - 1):
            if s[i] != s[i + 1] and cnt[s[i]] == int(s[i]) and cnt[s[i + 1]] == int(s[i + 1]):
                return s[i:i + 2]
        return ""


if __name__ == '__main__':
    pass
