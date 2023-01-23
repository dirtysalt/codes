#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def largestInteger(self, num: int) -> int:
        parity = []
        d = [[], []]
        while num:
            x = num % 10
            sel = x % 2
            parity.append(sel)
            d[sel].append(x)
            num = num // 10

        d[0].sort()
        d[1].sort()
        ans = 0
        while parity:
            sel = parity.pop()
            ans = ans * 10 + d[sel].pop()
        return ans


if __name__ == '__main__':
    pass
