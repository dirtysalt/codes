#!/usr/bin/env python3
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def minElements(self, nums: List[int], limit: int, goal: int) -> int:
        now = sum(nums)
        diff = abs(goal - now)
        ans = (diff + limit - 1) // limit
        return ans
