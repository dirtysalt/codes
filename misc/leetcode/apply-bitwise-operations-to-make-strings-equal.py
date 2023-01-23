#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def makeStringsEqual(self, s: str, target: str) -> bool:
        c = 0
        n = len(s)
        for i in range(n):
            if s[i] == '1':
                c += 1

        for i in range(n):
            if s[i] != target[i] and s[i] == '0':
                if c > 0:  # 01 -> 11
                    # s[i] == '1'
                    c += 1
                else:
                    return False

        for i in range(n):
            if s[i] != target[i] and s[i] == '1':
                if c > 1:  # 11 -> 01
                    # s[i] == '0':
                    c -= 1
                else:
                    return False

        return True


if __name__ == '__main__':
    pass
