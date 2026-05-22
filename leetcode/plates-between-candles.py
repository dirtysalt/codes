#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        n = len(s)
        lps, rps = [-1] * n, [-1] * n
        acc = [0] * (n + 1)

        p = -1
        for i in reversed(range(n)):
            if s[i] == '|':
                p = i
            rps[i] = p
        p = -1
        for i in range(n):
            if s[i] == '|':
                p = i
            lps[i] = p

        for i in range(n):
            v = 0
            if s[i] == '*':
                v = 1
            acc[i + 1] = acc[i] + v

        ans = []
        for x, y in queries:
            x2 = rps[x]
            y2 = lps[y]
            res = 0
            if (x2 != -1 and y2 != -1 and y2 > x2):
                res = acc[y2 + 1] - acc[x2]
            ans.append(res)

        return ans


if __name__ == '__main__':
    pass
