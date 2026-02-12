#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt


class Solution:
    def isValid(self, word: str) -> bool:
        if len(word) < 3: return False
        c0, c1 = 0, 0
        for c in word:
            import string
            if c not in string.digits and c not in string.ascii_letters:
                return False
            if c in string.ascii_letters:
                if c.lower() in 'aeiou':
                    c0 += 1
                else:
                    c1 += 1
        return c0 > 0 and c1 > 0


if __name__ == '__main__':
    pass
