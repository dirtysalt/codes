#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def maximumCostSubstring(self, s: str, chars: str, vals: List[int]) -> int:
        w = {i: i + 1 for i in range(26)}
        for c, v in zip(chars, vals):
            c2 = ord(c) - ord('a')
            w[c2] = v

        r = 0
        ans = 0
        for c in s:
            c2 = ord(c) - ord('a')
            r += w[c2]
            if r < 0:
                r = 0
            ans = max(ans, r)
        return ans


if __name__ == '__main__':
    pass
