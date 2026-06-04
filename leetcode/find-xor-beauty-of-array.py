#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def xorBeauty(self, nums: List[int]) -> int:
        ans = 0
        for x in nums:
            ans = ans ^ x
        return ans


if __name__ == '__main__':
    pass
