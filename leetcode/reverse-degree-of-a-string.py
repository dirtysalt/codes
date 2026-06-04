#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt


class Solution:
    def reverseDegree(self, s: str) -> int:
        ans = 0
        for i, c in enumerate(s):
            ans += (i + 1) * (26 + ord('a') - ord(c))
        return ans


if __name__ == '__main__':
    pass
