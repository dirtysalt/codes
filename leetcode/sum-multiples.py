#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def sumOfMultiples(self, n: int) -> int:
        def ok(x):
            for y in (3, 5, 7):
                if x % y == 0:
                    return True
            return False

        ans = 0
        for x in range(2, n + 1):
            if ok(x):
                ans += x
        return ans


if __name__ == '__main__':
    pass
