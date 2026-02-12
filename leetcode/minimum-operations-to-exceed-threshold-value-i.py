#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        ans = len([x for x in nums if x < k])
        return ans


if __name__ == '__main__':
    pass
