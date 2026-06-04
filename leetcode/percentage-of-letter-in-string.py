#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def percentageLetter(self, s: str, letter: str) -> int:
        n = len(s)
        t = 0
        for c in s:
            if c == letter:
                t += 1
        return t * 100 // n


if __name__ == '__main__':
    pass
