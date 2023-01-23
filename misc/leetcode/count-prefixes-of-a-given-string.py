#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def countPrefixes(self, words: List[str], s: str) -> int:
        ans = 0
        for w in words:
            if s.startswith(w):
                ans += 1
        return ans


if __name__ == '__main__':
    pass
