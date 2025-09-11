#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        i = 1
        d = -1
        for _ in range(time):
            if i in (1, n):
                d = -d
            i += d
        return i


if __name__ == '__main__':
    pass
