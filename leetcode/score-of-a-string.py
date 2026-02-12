#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt


class Solution:
    def scoreOfString(self, s: str) -> int:
        ans = 0
        for i in range(1, len(s)):
            r = abs(ord(s[i]) - ord(s[i - 1]))
            ans += r
        return ans


if __name__ == '__main__':
    pass
