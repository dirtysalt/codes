#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:

    def __init__(self, w: List[int]):
        n = len(w)
        self.w = w
        for i in range(n - 1):
            w[i + 1] += w[i]

    def pickIndex(self) -> int:
        import random
        w = self.w
        x = random.randint(1, w[-1])
        s, e = 0, len(w) - 1
        while s <= e:
            m = (s + e) // 2
            if w[m] >= x:
                e = m - 1
            else:
                s = m + 1
        ans = s
        return ans

# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
