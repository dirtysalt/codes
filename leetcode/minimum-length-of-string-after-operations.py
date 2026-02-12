#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt


class Solution:
    def minimumLength(self, s: str) -> int:
        from collections import Counter
        cnt = Counter(s)
        ans = 0
        for k, c in cnt.items():
            c = c % 2
            if c == 0: c += 2
            ans += c
        return ans


if __name__ == '__main__':
    pass
