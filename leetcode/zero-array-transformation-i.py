#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        event = []
        for i in range(len(nums)):
            event.append((i, 2))
        for l, r in queries:
            event.append((l, 0))
            event.append((r + 1, 1))

        event.sort()
        d = 0
        for i, t in event:
            if t == 0:
                d += 1
            elif t == 1:
                d -= 1
            else:
                if nums[i] > d:
                    return False
        return True


if __name__ == '__main__':
    pass
