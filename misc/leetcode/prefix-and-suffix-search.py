#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class WordFilter:

    def __init__(self, words: List[str]):
        from collections import defaultdict
        pfx = defaultdict(list)
        sfx = defaultdict(list)

        for i in range(len(words)):
            w = words[i]
            for j in range(len(w) + 1):
                a, b = w[:j], w[j:]
                pfx[a].append(i)
                sfx[b].append(i)
        self.pfx = pfx
        self.sfx = sfx
        print(pfx, sfx)

    def f(self, prefix: str, suffix: str) -> int:
        xs = self.pfx[prefix]
        ys = self.sfx[suffix]
        i, j = len(xs) - 1, len(ys) - 1
        while i >= 0 and j >= 0:
            if xs[i] == ys[j]:
                return xs[i]
            elif xs[i] > ys[j]:
                i -= 1
            else:
                j -= 1
        return -1

# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(prefix,suffix)
