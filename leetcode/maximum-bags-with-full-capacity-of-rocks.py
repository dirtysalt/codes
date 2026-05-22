#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        rs = [x - y for (x, y) in zip(capacity, rocks)]
        rs.sort()

        ans = 0
        for i in range(len(rs)):
            if additionalRocks < rs[i]:
                break
            ans += 1
            additionalRocks -= rs[i]

        return ans


if __name__ == '__main__':
    pass
