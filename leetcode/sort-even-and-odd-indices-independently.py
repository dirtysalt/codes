#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def sortEvenOdd(self, nums: List[int]) -> List[int]:
        a = []
        b = []
        for i in range(len(nums)):
            x = nums[i]
            if i % 2 == 0:
                a.append(x)
            else:
                b.append(x)

        a.sort(reverse=True)
        b.sort()
        ans = []
        while a and b:
            ans.append(a.pop())
            ans.append(b.pop())
        while a:
            ans.append(a.pop())
        while b:
            ans.append(b.pop())
        return ans


if __name__ == '__main__':
    pass
