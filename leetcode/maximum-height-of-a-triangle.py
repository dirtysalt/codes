#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def maxHeightOfTriangle(self, red: int, blue: int) -> int:
        def test(r, b):
            n = 1
            while True:
                if r >= n:
                    r -= n
                    n += 1
                else:
                    break
                if b >= n:
                    b -= n
                    n += 1
                else:
                    break
            return n - 1

        a = test(red, blue)
        b = test(blue, red)
        return max(a, b)


if __name__ == '__main__':
    pass
