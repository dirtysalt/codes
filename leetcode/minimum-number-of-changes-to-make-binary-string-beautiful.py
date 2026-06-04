#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def minChanges(self, s: str) -> int:

        n = len(s)
        last = 0
        ans = 0
        for i in range(n):
            if s[i] != s[last]:
                sz = (i - last)
                if sz % 2 == 1:
                    ans += 1
                    last = i + 1
                else:
                    last = i
        return ans


if __name__ == '__main__':
    pass
