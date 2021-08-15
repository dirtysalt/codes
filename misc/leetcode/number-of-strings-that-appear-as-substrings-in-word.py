#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        ans = 0
        for p in patterns:
            if word.find(p) != -1:
                ans += 1
        return ans


if __name__ == '__main__':
    pass
