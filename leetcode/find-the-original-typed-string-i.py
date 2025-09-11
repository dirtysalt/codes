#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt


class Solution:
    def possibleStringCount(self, word: str) -> int:
        tail, rep = None, 1
        ans = 1
        for c in word:
            if tail != c:
                ans += (rep - 1)
                rep = 1
                tail = c
            else:
                rep += 1
        ans += (rep - 1)
        return ans


if __name__ == '__main__':
    pass
