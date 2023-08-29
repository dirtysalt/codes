#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt
import functools


class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:

        @functools.cache
        def search(i, d):
            if i == len(moves): return abs(d)

            ans = 0
            if moves[i] in 'L_':
                c = search(i + 1, d - 1)
                ans = max(ans, c)

            if moves[i] in 'R_':
                c = search(i + 1, d + 1)
                ans = max(ans, c)

            return ans

        ans = search(0, 0)
        return ans


if __name__ == '__main__':
    pass
