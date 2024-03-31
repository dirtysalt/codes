#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt


class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        ans = numBottles
        empty = numBottles
        while empty >= numExchange:
            empty -= numExchange
            ans += 1
            empty += 1
            numExchange += 1
        return ans


if __name__ == '__main__':
    pass
