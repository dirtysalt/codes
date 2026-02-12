#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Trie:
    def __init__(self, wordsContainer):
        self.stop = None
        self.child = [None] * 26
        self.wordsContainer = wordsContainer

    def add(self, s, idx):
        if self.stop is None:
            self.stop = idx
        elif len(self.wordsContainer[self.stop]) > len(self.wordsContainer[idx]):
            self.stop = idx

        if not s: return

        c = ord(s[0]) - ord('a')
        if self.child[c] is None:
            self.child[c] = Trie(self.wordsContainer)
        self.child[c].add(s[1:], idx)

    def search(self, s):
        if not s: return self.stop
        c = ord(s[0]) - ord('a')
        if self.child[c] is not None:
            return self.child[c].search(s[1:])
        return self.stop


class Solution:
    def stringIndices(self, wordsContainer: List[str], wordsQuery: List[str]) -> List[int]:
        default = 0
        for i in range(len(wordsContainer)):
            if len(wordsContainer[i]) < len(wordsContainer[default]):
                default = i

        trie = Trie(wordsContainer)
        for idx in range(len(wordsContainer)):
            s = wordsContainer[idx][::-1]
            trie.add(s, idx)

        ans = []
        for q in wordsQuery:
            q = q[::-1]
            res = trie.search(q)
            if res is None: res = default
            ans.append(res)

        return ans


if __name__ == '__main__':
    pass
