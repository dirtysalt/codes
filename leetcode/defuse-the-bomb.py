#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n = len(code)
        if k == 0:
            return [0] * n
        if k > 0:
            d = 1
        else:
            d = -1
            k = -k

        ans = []
        for i in range(n):
            acc = 0
            for k2 in range(k):
                j = i + (1 + k2) * d
                acc += code[(j + n) % n]
            ans.append(acc)
        return ans
