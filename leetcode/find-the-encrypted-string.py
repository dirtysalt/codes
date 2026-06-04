#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt


class Solution:
    def getEncryptedString(self, s: str, k: int) -> str:
        n = len(s)
        k = k % n
        return s[k:] + s[:k]


if __name__ == '__main__':
    pass
