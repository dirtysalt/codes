#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        n = len(arr)
        xor = [0] * (n + 1)
        for i in range(n):
            xor[i + 1] = arr[i] ^ xor[i]

        ans = 0
        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j, n):
                    a = xor[j] ^ xor[i]
                    b = xor[k + 1] ^ xor[j]
                    if a == b:
                        ans += 1
        return ans
