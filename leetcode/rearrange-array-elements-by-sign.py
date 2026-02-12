#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        a = [x for x in nums if x > 0]
        b = [x for x in nums if x < 0]
        ans = []
        for i in range(len(a)):
            ans.append(a[i])
            ans.append(b[i])
        return ans


if __name__ == '__main__':
    pass
