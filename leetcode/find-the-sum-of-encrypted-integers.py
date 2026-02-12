#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def sumOfEncryptedInt(self, nums: List[int]) -> int:
        def tox(x):
            rep = 0
            d = 0
            while x:
                d = max(d, x % 10)
                x = x // 10
                rep += 1
            value = 0
            for _ in range(rep):
                value = value * 10 + d
            return value

        ans = 0
        for x in nums:
            ans += tox(x)
        return ans


if __name__ == '__main__':
    pass
