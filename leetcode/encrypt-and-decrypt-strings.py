#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt
import functools
from typing import List


class Encrypter:

    def __init__(self, keys: List[str], values: List[str], dictionary: List[str]):
        self.keys = keys
        self.values = values
        self.ki = {keys[i]: i for i in range(len(keys))}
        from collections import defaultdict
        self.vi = defaultdict(list)
        for i in range(len(values)):
            self.vi[values[i]].append(i)
        self.prefix = defaultdict(set)

        for d in dictionary:
            sz = len(d)
            for i in range(sz):
                w = d[:i + 1]
                self.prefix[sz].add(w)

    def encrypt(self, word1: str) -> str:
        ans = []
        for c in word1:
            i = self.ki[c]
            v = self.values[i]
            ans.append(v)
        return ''.join(ans)

    @functools.lru_cache(maxsize=None)
    def decrypt(self, word2: str) -> int:
        sz = len(word2) // 2
        ans = set([""])
        for i in range(0, len(word2), 2):
            c = word2[i:i + 2]
            newans = set()
            for j in self.vi[c]:
                k = self.keys[j]
                for x in ans:
                    y = x + k
                    if y not in self.prefix[sz]: continue
                    newans.add(y)
            ans = newans
        return len(ans)


# Your Encrypter object will be instantiated and called as such:
# obj = Encrypter(keys, values, dictionary)
# param_1 = obj.encrypt(word1)
# param_2 = obj.decrypt(word2)

if __name__ == '__main__':
    pass
