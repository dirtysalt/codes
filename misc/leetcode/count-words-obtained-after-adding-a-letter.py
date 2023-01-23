#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def wordCount(self, startWords: List[str], targetWords: List[str]) -> int:

        def tobits(w):
            val = 0
            for c in w:
                i = ord(c) - ord('a')
                val = val | (1 << i)
            return val

        from collections import Counter
        counter = Counter()
        used = set()
        for i in range(len(targetWords)):
            w = targetWords[i]
            b = tobits(w)
            counter[b] += 1

        for w in startWords:
            b = tobits(w)
            for i in range(26):
                if (b & (1 << i)): continue
                b2 = b | (1 << i)
                used.add(b2)

        ans = 0
        for b in used:
            ans += counter[b]
        return ans


if __name__ == '__main__':
    pass
