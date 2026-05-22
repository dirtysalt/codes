#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def greatestLetter(self, s: str) -> str:
        ok = [0] * 26
        for c in s:
            x = ord(c)
            if ord('a') <= x <= ord('z'):
                ok[x - ord('a')] |= 1
            if ord('A') <= x <= ord('Z'):
                ok[x - ord('A')] |= 2

        for i in reversed(range(26)):
            if ok[i] == 3:
                return chr(i + ord('A'))
        return ''


if __name__ == '__main__':
    pass
