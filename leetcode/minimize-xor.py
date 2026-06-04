#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        def getbits(x):
            b = [0] * 32
            t = 0
            for i in range(32):
                if (x >> i) & 0x1:
                    b[i] += 1
                    t += 1
            return b, t

        _, t = getbits(num2)
        b, _ = getbits(num1)

        ans = 0
        if t:
            for i in reversed(range(32)):
                if t > 0 and b[i] == 1:
                    t -= 1
                    ans = ans | (1 << i)
            for i in range(32):
                if t > 0 and b[i] == 0:
                    t -= 1
                    ans = ans | (1 << i)
        return ans


if __name__ == '__main__':
    pass
