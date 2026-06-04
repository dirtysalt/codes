#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def minimumSum(self, n: int, k: int) -> int:
        ss = set()
        x = 1
        for _ in range(n):
            while True:
                exp = k - x
                if exp not in ss:
                    ss.add(x)
                    x += 1
                    break
                x += 1
        return sum(ss)


if __name__ == '__main__':
    pass
