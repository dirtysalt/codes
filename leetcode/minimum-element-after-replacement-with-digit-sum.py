#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def minElement(self, nums: List[int]) -> int:
        def convert(x):
            r = 0
            while x:
                r += x % 10
                x = x // 10
            return r

        return min([convert(x) for x in nums])


if __name__ == '__main__':
    pass
