#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:

        import functools
        @functools.cache
        def search(i):
            if i == len(s): return 0
            ans = len(s)
            for j in range(i, len(s)):
                v = s[i:j + 1]
                c = search(j + 1)
                if v not in dictionary:
                    c += j - i + 1
                ans = min(ans, c)
            return ans

        ans = search(0)
        return ans


if __name__ == '__main__':
    pass
