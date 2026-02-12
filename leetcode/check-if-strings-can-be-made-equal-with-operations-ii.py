#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def checkStrings(self, s1: str, s2: str) -> bool:
        for i in range(0, 2):
            a = ''.join(sorted(s1[i::2]))
            b = ''.join(sorted(s2[i::2]))
            if a != b: return False
        return True


if __name__ == '__main__':
    pass
