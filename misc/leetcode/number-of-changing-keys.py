#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def countKeyChanges(self, s: str) -> int:
        s = s.lower()
        x = s[0]
        ans = 0
        for c in s:
            if c != x:
                ans += 1
                x = c
        return ans


if __name__ == '__main__':
    pass
