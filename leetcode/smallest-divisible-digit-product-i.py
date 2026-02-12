#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt


class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        def prod(x):
            res = 1
            while x:
                res *= x % 10
                x = x // 10
            return res

        ans = n
        while True:
            p = prod(ans)
            if p % t == 0:
                return ans
            ans += 1


if __name__ == '__main__':
    pass
