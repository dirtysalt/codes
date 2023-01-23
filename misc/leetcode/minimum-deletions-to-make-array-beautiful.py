#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def minDeletion(self, nums: List[int]) -> int:
        last = None
        ans = 0
        for x in nums:
            if last is None:
                last = x
            elif last == x:
                ans += 1
            else:
                last = None
        if last is not None:
            ans += 1
        return ans


if __name__ == '__main__':
    pass
