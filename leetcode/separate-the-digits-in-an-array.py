#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        ans = []
        for x in nums:
            tmp = []
            while x:
                tmp.append(x % 10)
                x = x // 10
            tmp = tmp[::-1]
            ans += tmp
        return ans


if __name__ == '__main__':
    pass
