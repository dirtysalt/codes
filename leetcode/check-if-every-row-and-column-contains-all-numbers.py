#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:

        def ok(M):
            n = len(M)
            for i in range(n):
                s = set(M[i])
                if len(s) != n:
                    return False
            return True

        return ok(matrix) and ok(list(zip(*matrix)))


if __name__ == '__main__':
    pass
