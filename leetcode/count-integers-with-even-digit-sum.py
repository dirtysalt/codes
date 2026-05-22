#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def countEven(self, num: int) -> int:
        def ok(x):
            t = 0
            while x:
                t += x % 10
                x = x // 10
            return t % 2 == 0

        ans = 0
        for x in range(2, num + 1):
            if ok(x):
                ans += 1
        return ans


if __name__ == '__main__':
    pass
