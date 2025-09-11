#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        a = []
        b = []
        c = 0

        for x in nums:
            if x < pivot:
                a.append(x)
            elif x > pivot:
                b.append(x)
            else:
                c += 1

        ans = a + [pivot] * c + b
        return ans


if __name__ == '__main__':
    pass
