#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def checkString(self, s: str) -> bool:
        i = 0
        while i < len(s) and s[i] == 'a':
            i += 1
        while i < len(s) and s[i] == 'b':
            i += 1
        return i == len(s)


if __name__ == '__main__':
    pass
