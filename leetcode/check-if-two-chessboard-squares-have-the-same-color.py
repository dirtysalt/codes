#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt


class Solution:
    def checkTwoChessboards(self, coordinate1: str, coordinate2: str) -> bool:
        def f(s):
            a, b = s[0], s[1]
            x = (ord(a) - ord('a')) % 2
            y = int(b) % 2
            if y % 2 == 1:
                x = 1 - x
            return x

        return f(coordinate1) == f(coordinate2)


if __name__ == '__main__':
    pass
