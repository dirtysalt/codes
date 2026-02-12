#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        for w in words:
            if w == w[::-1]:
                return w
        return ""


if __name__ == '__main__':
    pass
