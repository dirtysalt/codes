#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def addMinimum(self, word: str) -> int:
        n = len(word)
        i = 0
        ans = 0
        while i < n:
            ch = word[i]

            if ch == 'a':
                if word[i + 1:i + 3] == 'bc':
                    i += 3
                elif word[i + 1:i + 2] in ('b', 'c'):
                    i += 2
                    ans += 1
                else:
                    i += 1
                    ans += 2

            elif ch == 'b':
                ans += 1
                if word[i + 1:i + 2] == 'c':
                    i += 2
                else:
                    i += 1
                    ans += 1

            else:
                i += 1
                ans += 2
        return ans


if __name__ == '__main__':
    pass
