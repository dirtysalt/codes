#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt


class Solution:
    def compressedString(self, word: str) -> str:
        ans = ''
        i = 0
        while i < len(word):
            j = i
            while j < len(word) and word[j] == word[i]:
                j += 1
            c = word[i]
            sz = j - i
            i = j

            while sz:
                ans += str(min(sz, 9))
                ans += c
                sz -= min(sz, 9)
        return ans


if __name__ == '__main__':
    pass
