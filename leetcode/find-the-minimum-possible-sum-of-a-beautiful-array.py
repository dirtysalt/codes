#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def minimumPossibleSum(self, n: int, target: int) -> int:
        ss = set()
        i = 1
        while len(ss) < n:
            if target - i not in ss:
                ss.add(i)
            i += 1
        return sum(ss)


if __name__ == '__main__':
    pass
