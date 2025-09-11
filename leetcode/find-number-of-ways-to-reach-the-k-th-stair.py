#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt


class Solution:
    def waysToReachStair(self, k: int) -> int:

        import functools
        @functools.cache
        def dfs(i, jump, back):
            if i >= k + 4: return 0
            r = (i == k)
            r += dfs(i + 2 ** jump, jump + 1, 0)
            if back == 0:
                r += dfs(i - 1, jump, 1)
            return r

        ans = dfs(1, 0, 0)
        return ans


if __name__ == '__main__':
    pass
