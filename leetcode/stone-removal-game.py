#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt


class Solution:
    def canAliceWin(self, n: int) -> bool:
        ans = False
        d = 10
        while n >= d:
            n -= d
            ans = not ans
            d -= 1
            if d == 0:
                break
        return ans


if __name__ == '__main__':
    pass
