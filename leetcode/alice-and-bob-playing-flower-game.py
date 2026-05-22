#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def flowerGame(self, n: int, m: int) -> int:
        a = (n + 1) // 2
        b = m // 2
        c0 = a * b

        a = (m + 1) // 2
        b = n // 2
        c1 = a * b

        return c0 + c1


if __name__ == '__main__':
    pass
