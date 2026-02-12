#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        def ok(a, b):
            if b.startswith(a) and b.endswith(a):
                return 1
            return 0

        n = len(words)
        ans = 0
        for i in range(n):
            for j in range(i + 1, n):
                if ok(words[i], words[j]):
                    ans += 1
        return ans


if __name__ == '__main__':
    pass
