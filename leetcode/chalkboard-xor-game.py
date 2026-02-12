#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def xorGame(self, nums: List[int]) -> bool:
        v = 0
        for x in nums:
            v = v ^ x
        if v == 0:
            return True
        return len(nums) % 2 == 0
