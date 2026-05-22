#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def findMinimumOperations(self, s1: str, s2: str, s3: str) -> int:
        sz = min(len(s1), len(s2), len(s3))
        for i in reversed(range(1, sz + 1)):
            if s1[:i] == s2[:i] == s3[:i]:
                return len(s1) + len(s2) + len(s3) - 3 * i
        return -1


if __name__ == '__main__':
    pass
