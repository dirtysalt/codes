#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def minimumBeautifulSubstrings(self, s: str) -> int:
        MAX = (1 << len(s)) - 1
        ss = set()
        x = 1
        while x <= MAX:
            # remove '0b'
            ss.add(bin(x)[2:])
            x = x * 5

        from functools import cache
        INF = 100000

        @cache
        def search(i):
            if i == len(s): return 0
            if s[i] == '0': return INF

            ans = INF
            for j in range(i, len(s)):
                if s[i:j + 1] in ss:
                    c = search(j + 1)
                    ans = min(ans, c + 1)

            return ans

        ans = search(0)
        if ans == INF: ans = -1
        return ans


if __name__ == '__main__':
    pass
