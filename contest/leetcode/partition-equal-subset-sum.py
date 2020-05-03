#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt


from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        tt = sum(nums)
        if tt % 2 == 1:
            return False

        dp = {0}
        for x in nums:
            tmp = []
            for k in dp:
                tmp.append(x + k)
            dp.update(tmp)

        ans = (tt // 2) in dp
        return ans
