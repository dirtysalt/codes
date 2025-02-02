#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt


class Solution:
    def maxDifference(self, s: str) -> int:
        cnt = [0] * 26
        for c in s:
            cnt[ord(c) - ord('a')] += 1

        k1, k2 = 0, 1000
        for x in cnt:
            if x == 0: continue
            if x % 2 == 1:
                k1 = max(k1, x)
            else:
                k2 = min(k2, x)
        return k1 - k2


if __name__ == '__main__':
    pass
