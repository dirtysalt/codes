#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def minimumMoves(self, s: str) -> int:
        n = len(s)
        i = 0
        ans = 0
        while i < n:
            if s[i] == 'X':
                ans += 1
                i += 3
            else:
                i += 1
        return ans


if __name__ == '__main__':
    pass
