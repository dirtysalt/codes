#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        n = len(s)

        for (d, am) in shift:
            am = am % n
            if d == 1:
                am = n - am

            s2 = s + s
            s = s2[am: am + n]
        return s
