#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def punishmentNumber(self, n: int) -> int:

        import functools

        @functools.cache
        def search(s):
            if not s: return {0}

            ans = set()
            for i in range(len(s)):
                x = int(s[:i + 1])
                rs = search(s[i + 1:])
                for r in rs:
                    ans.add(x + r)
            return ans

        def check(x):
            values = search(str(x * x))
            if x in values:
                return x
            return 0

        ans = 0
        for i in range(1, n + 1):
            x = check(i)
            ans += x * x
        return ans


if __name__ == '__main__':
    pass
