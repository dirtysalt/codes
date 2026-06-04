#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        cnt = [0] * 501
        for x in nums:
            cnt[x] += 1
        for x in cnt:
            if x % 2 != 0:
                return False
        return True


if __name__ == '__main__':
    pass
