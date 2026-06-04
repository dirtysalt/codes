#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        ans = 0
        for x in range(1, min(a, b) + 1):
            if a % x == 0 and b % x == 0:
                ans += 1
        return ans


if __name__ == '__main__':
    pass
