#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def reorderedPowerOf2(self, N: int) -> bool:
        def to_ft(x):
            ft = [0] * 10
            while x:
                ft[x % 10] += 1
                x //= 10
            return ft

        ft = to_ft(N)
        for i in range(0, 32):
            x = 1 << i
            ft_x = to_ft(x)
            if ft == ft_x:
                return True
        return False
