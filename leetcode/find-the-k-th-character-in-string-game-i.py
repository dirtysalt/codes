#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt


class Solution:
    def kthCharacter(self, k: int) -> str:
        def change(s):
            return ''.join(chr((ord(x) - ord('a') + 1) % 26 + ord('a')) for x in s)

        s = 'a'
        while len(s) < k:
            s += change(s)

        return s[k - 1]


if __name__ == '__main__':
    pass
