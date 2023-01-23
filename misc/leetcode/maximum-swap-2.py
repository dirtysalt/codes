#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def maximumSwap(self, num: int) -> int:
        i = 0

        x = num
        most_idx = -1
        most_value = -1
        swap = None
        while x:
            d = x % 10
            if d > most_value:
                most_value = d
                most_idx = i
            elif d < most_value:
                swap = i, d, most_idx, most_value
            i += 1
            x //= 10

        ans = num
        if swap:
            i, d, i2, d2 = swap
            ans += (d2 - d) * (10 ** i) - (d2 - d) * (10 ** i2)
        return ans
