#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def repeatedCharacter(self, s: str) -> str:
        mask = [0] * 26
        for c in s:
            c2 = ord(c) - ord('a')
            if mask[c2] == 0:
                mask[c2] = 1
            else:
                return c
        return ''


if __name__ == '__main__':
    pass
