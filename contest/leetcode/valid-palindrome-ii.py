#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def validPalindrome(self, s: str) -> bool:
        i, j = 0, len(s) - 1

        while i <= j:
            if s[i] != s[j]:
                x = s[i:j]
                if x == x[::-1]:
                    return True
                x = s[i + 1:j + 1]
                if x == x[::-1]:
                    return True
                return False
            else:
                i += 1
                j -= 1
        return True
