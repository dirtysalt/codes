#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:

        def test(k):
            event = []
            for i in range(len(nums)):
                event.append((i, 2, nums[i]))
            for l, r, v in queries[:k]:
                event.append((l, 0, v))
                event.append((r + 1, 1, v))

            event.sort()
            d = 0
            for i, t, v in event:
                if t == 0:
                    d += v
                elif t == 1:
                    d -= v
                else:
                    if v > d:
                        return False
            return True

        s, e = 0, len(queries)
        while s <= e:
            m = (s + e) // 2
            if test(m):
                e = m - 1
            else:
                s = m + 1
        if s > len(queries):
            return -1
        return s


if __name__ == '__main__':
    pass
