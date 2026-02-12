#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def canAliceWin(self, nums: List[int]) -> bool:
        total = sum(nums)
        a = sum([x for x in nums if x < 10])
        b = total - a
        return a > b or b > a


if __name__ == '__main__':
    pass
