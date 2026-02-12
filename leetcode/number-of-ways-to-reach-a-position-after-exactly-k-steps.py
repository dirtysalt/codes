#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def numberOfWays(self, startPos: int, endPos: int, k: int) -> int:
        MOD = 10 ** 9 + 7

        import functools
        @functools.cache
        def search(p, k):
            if (p + k) < endPos or (p - k) > endPos:
                return 0

            if (p + k) == endPos or (p - k) == endPos:
                return 1

            ans = 0
            ans += search(p + 1, k - 1)
            ans += search(p - 1, k - 1)
            return ans

        ans = search(startPos, k)
        return ans % MOD


if __name__ == '__main__':
    pass
