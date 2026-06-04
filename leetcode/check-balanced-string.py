#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt


class Solution:
    def isBalanced(self, num: str) -> bool:
        res = [0] * 2
        now = 0
        for x in num:
            res[now] += int(x)
            now = 1 - now
        return res[0] == res[1]


if __name__ == '__main__':
    pass
