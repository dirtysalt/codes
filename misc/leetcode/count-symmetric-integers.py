#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        def check(x):
            tmp = []
            while x:
                tmp.append(x % 10)
                x = x // 10
            if len(tmp) % 2 != 0: return False
            a = sum(tmp[:len(tmp) // 2])
            b = sum(tmp[len(tmp) // 2:])
            return a == b

        ans = 0
        for x in range(low, high + 1):
            if check(x):
                ans += 1
        return ans


if __name__ == '__main__':
    pass
