#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def destroyTargets(self, nums: List[int], space: int) -> int:
        nums.sort()
        d = {}
        for x in nums:
            y = x % space
            if y not in d:
                d[y] = [x, 1]
            else:
                d[y][1] += 1

        count = 0
        ans = -1
        for y in d:
            x, dy = d[y]
            if dy >= count:
                if dy == count:
                    ans = min(ans, x)
                else:
                    ans = x
                count = dy

        return ans


if __name__ == '__main__':
    pass
