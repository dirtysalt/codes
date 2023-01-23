#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        d = set(nums)

        ans = -1
        for x in nums:
            if x > 0 and -x in d:
                ans = max(ans, x)
        return ans


if __name__ == '__main__':
    pass
