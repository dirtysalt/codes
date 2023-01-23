#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        ans = 0
        for i in range(32):
            x = (a >> i) & 0x1
            y = (b >> i) & 0x1
            z = (c >> i) & 0x1
            if (x | y) == z: continue
            if z == 0 and x == 1 and y == 1:
                ans += 2
            else:
                ans += 1
        return ans


if __name__ == '__main__':
    pass
