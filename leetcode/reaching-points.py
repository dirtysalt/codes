#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def reachingPoints(self, sx: int, sy: int, tx: int, ty: int) -> bool:
        if tx < sx or ty < sy:
            return False

        while True:
            m = (tx - sx) // ty
            tx -= m * ty
            n = (ty - sy) // tx
            ty -= n * tx
            if m == 0 and n == 0:
                break

        return sx == tx and sy == ty
