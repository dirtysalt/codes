#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        ans = 0
        t = 0
        for x in nums:
            if x == 0:
                t += 1
            else:
                ans += t * (t + 1) // 2
                t = 0
        ans += t * (t + 1) // 2
        return ans


if __name__ == '__main__':
    pass
