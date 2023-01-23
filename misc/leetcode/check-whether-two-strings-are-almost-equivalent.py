#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def checkAlmostEquivalent(self, word1: str, word2: str) -> bool:

        def build(w):
            cnt = [0] * 26
            for c in w:
                cnt[ord(c) - ord('a')] += 1
            return cnt

        c1 = build(word1)
        c2 = build(word2)

        for i in range(26):
            if abs(c1[i] - c2[i]) > 3:
                return False
        return True


if __name__ == '__main__':
    pass
