#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        tmp = []
        for x in nums:
            tmp.append((int(x), x))
        tmp.sort(key=lambda x: x[0])
        return tmp[-k][1]


if __name__ == '__main__':
    pass
