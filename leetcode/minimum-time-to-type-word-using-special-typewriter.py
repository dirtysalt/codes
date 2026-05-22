#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def minTimeToType(self, word: str) -> int:
        p = 0
        ans = 0
        for w in word:
            c = ord(w) - ord('a')
            x1 = (c - p + 26) % 26
            x2 = (p - c + 26) % 26
            ans += min(x1, x2) + 1
            p = c
        return ans


if __name__ == '__main__':
    pass
