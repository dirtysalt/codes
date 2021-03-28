#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def reinitializePermutation(self, n: int) -> int:
        init = list(range(n))
        ans = 0
        base = init
        while True:
            ans += 1
            a = base[::2] + base[1::2]
            if a == init:
                break
            base = a
        return ans
