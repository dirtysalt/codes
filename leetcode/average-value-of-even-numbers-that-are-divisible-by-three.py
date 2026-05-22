#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def averageValue(self, nums: List[int]) -> int:
        ss = []
        for x in nums:
            if x % 6 == 0:
                ss.append(x)

        if not ss:
            return 0
        return sum(ss) // len(ss)


if __name__ == '__main__':
    pass
