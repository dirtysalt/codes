#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def evenOddBit(self, n: int) -> List[int]:
        a, b = 0, 0
        i = 0
        while n:
            if n & 0x1:
                if i % 2 == 0:
                    a += 1
                else:
                    b += 1
            i += 1
            n = n // 2
        # if i % 2 == 0:
        #     a, b = b ,a
        return [a, b]


if __name__ == '__main__':
    pass
