#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List
from collections import Counter, defaultdict, deque
from functools import lru_cache
import heapq


class Solution:
    def minimumDeletions(self, word: str, k: int) -> int:
        from collections import Counter
        cnt = Counter(word)
        freq = list(cnt.values())
        freq.sort()

        def test(xs):
            ans = 0
            for x in xs:
                if x > (xs[0] + k):
                    ans += x - xs[0] - k
            return ans

        ans = 1 << 30
        cut = 0
        for i in range(len(freq)):
            r = test(freq[i:])
            ans = min(r + cut, ans)
            cut += freq[i]

        return ans


if __name__ == '__main__':
    pass
