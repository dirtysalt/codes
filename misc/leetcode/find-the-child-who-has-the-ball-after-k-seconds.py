#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt


class Solution:
    def numberOfChild(self, n: int, k: int) -> int:
        idx = 0
        delta = -1
        for _ in range(k):
            if idx in (0, n - 1):
                delta = -delta
            idx += delta
        return idx


if __name__ == '__main__':
    pass
