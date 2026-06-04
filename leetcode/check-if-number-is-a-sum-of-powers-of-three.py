#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        values = set([0])
        y = 1
        while y <= n:
            update = []
            for v in values:
                update.append(v + y)
            values.update(update)
            y = 3 * y
        return n in values
