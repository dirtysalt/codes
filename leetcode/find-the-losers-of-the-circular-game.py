#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def circularGameLosers(self, n: int, k: int) -> List[int]:
        bits = [0] * n
        p, p2 = 0, k
        while bits[p] == 0:
            bits[p] = 1
            p += p2
            p2 += k
            p = p % n
        ans = []
        for i in range(n):
            if bits[i] == 0:
                ans.append(i + 1)
        return ans


if __name__ == '__main__':
    pass
