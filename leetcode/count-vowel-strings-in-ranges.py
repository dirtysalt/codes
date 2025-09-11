#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        n = len(words)
        acc = [0] * (n + 1)
        for i in range(n):
            w = words[i]
            v = 0
            if w[0] in 'aeiou' and w[-1] in 'aeiou':
                v += 1
            acc[i + 1] = acc[i] + v

        ans = []
        for l, r in queries:
            ans.append(acc[r + 1] - acc[l])
        return ans


if __name__ == '__main__':
    pass
