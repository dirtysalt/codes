#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def minMovesToCaptureTheQueen(self, a: int, b: int, c: int, d: int, e: int, f: int) -> int:
        # rook to attack
        if a == e or b == f:
            s1, s2 = 0, 0
            if a == e:
                D = abs(f - b)
                s2 = (f - b) // D
            else:
                D = abs(e - a)
                s1 = (e - a) // D
            # bishop on way.
            on_way = False
            for i in range(D):
                if (a + i * s1) == c and (b + i * s2) == d:
                    on_way = True
                    break
            return 2 if on_way else 1

        # bishop to attack
        d1 = (e - c)
        d2 = (f - d)
        if abs(d1) == abs(d2):
            D = abs(d1)
            s1, s2 = d1 // D, d2 // D
            # rook on way.
            on_way = False
            for i in range(D):
                if (c + i * s1) == a and (d + i * s2) == b:
                    on_way = True
                    break
            return 2 if on_way else 1

        return 2


if __name__ == '__main__':
    pass
