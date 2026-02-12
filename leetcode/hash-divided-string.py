#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt


class Solution:
    def stringHash(self, s: str, k: int) -> str:
        def f(s):
            h = 0
            for c in s:
                h += ord(c) - ord('a')
            h = h % 26
            return chr(h + ord('a'))

        n = len(s)
        ans = []
        for i in range(n // k):
            c = f(s[i * k:i * k + k])
            ans.append(c)
        return ''.join(ans)


if __name__ == '__main__':
    pass
