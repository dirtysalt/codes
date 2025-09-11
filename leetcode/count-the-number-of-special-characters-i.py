#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt


class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        ans = 0
        import string
        for c in string.ascii_lowercase:
            if c in word and c.upper() in word:
                ans += 1
        return ans


if __name__ == '__main__':
    pass
