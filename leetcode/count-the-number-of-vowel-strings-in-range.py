#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def vowelStrings(self, words: List[str], left: int, right: int) -> int:
        def isok(c):
            return c in 'aeiou'

        ans = 0
        for i in range(left, right + 1):
            w = words[i]
            if isok(w[0]) and isok(w[-1]):
                ans += 1
        return ans


if __name__ == '__main__':
    pass
