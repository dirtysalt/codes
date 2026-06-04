#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def countAsterisks(self, s: str) -> int:
        ans = 0
        t = 0
        for c in s:
            if c == '|':
                t += 1
            elif t % 2 == 0:
                if c == '*':
                    ans += 1
        return ans


if __name__ == '__main__':
    pass
