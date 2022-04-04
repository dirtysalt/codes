#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        ans = 0
        x = start ^ goal
        while x:
            if x & 0x1:
                ans += 1
            x = x >> 1
        return ans


if __name__ == '__main__':
    pass
