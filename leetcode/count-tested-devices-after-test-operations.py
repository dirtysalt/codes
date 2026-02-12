#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def countTestedDevices(self, batteryPercentages: List[int]) -> int:
        ans = 0
        sub = 0
        for x in batteryPercentages:
            x -= sub
            if x > 0:
                ans += 1
                sub += 1
        return ans


if __name__ == '__main__':
    pass
