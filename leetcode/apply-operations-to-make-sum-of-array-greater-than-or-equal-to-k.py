#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt


class Solution:
    def minOperations(self, k: int) -> int:
        ans = 1 << 30
        for i in range(k + 1):
            value = 1 + i
            rep = (k + value - 1) // value
            c = i + rep - 1
            ans = min(ans, c)
        return ans


if __name__ == '__main__':
    pass
