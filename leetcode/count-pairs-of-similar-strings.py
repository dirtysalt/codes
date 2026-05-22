#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def similarPairs(self, words: List[str]) -> int:
        def rep(w):
            s = list(set(w))
            s.sort()
            return ''.join(s)

        from collections import Counter
        cnt = Counter()
        for w in words:
            rw = rep(w)
            cnt[rw] += 1

        ans = 0
        for k, v in cnt.items():
            ans += (v - 1) * v // 2
        return ans


if __name__ == '__main__':
    pass
