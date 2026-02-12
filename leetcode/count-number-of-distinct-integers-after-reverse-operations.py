#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        d = set(nums)

        def flip(x):
            ss = []
            while x:
                ss.append(x % 10)
                x = x // 10
            t = 0
            for x in ss:
                t = t * 10 + x
            return t

        for x in nums:
            y = flip(x)
            d.add(y)

        return len(d)


if __name__ == '__main__':
    pass
