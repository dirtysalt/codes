#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        def build(s):
            pos = [-1] * 26
            for i, c in enumerate(s):
                c = ord(c) - ord('a')
                pos[c] = i
            return pos

        p1 = build(s)
        p2 = build(t)
        ans = 0
        for x, y in zip(p1, p2):
            if x != -1 and y != -1:
                ans += abs(x - y)
        return ans


if __name__ == '__main__':
    pass
