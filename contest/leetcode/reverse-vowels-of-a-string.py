#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    """
    @param s: a string
    @return: reverse only the vowels of a string
    """

    def reverseVowels(self, s):
        # write your code here

        s = list(s)
        x, y = 0, len(s) - 1
        vowels = 'aeiouAEIOU'
        while x < y:
            while x < y and s[x] not in vowels:
                x += 1
            if x >= y:
                break
            while x < y and s[y] not in vowels:
                y -= 1
            if x >= y:
                break
            s[x], s[y] = s[y], s[x]
            x += 1
            y -= 1
        return ''.join(s)
