#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def minNumBooths(self, demand: List[str]) -> int:
        cnt = [0] * 26
        for s in demand:
            b = [0] * 26
            for c in s:
                b[ord(c) - ord('a')] += 1
            for i in range(26):
                cnt[i] = max(cnt[i], b[i])

        ans = sum(cnt)
        return ans


if __name__ == '__main__':
    pass
