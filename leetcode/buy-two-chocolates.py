#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        prices.sort()
        a = prices[0] + prices[1]
        if money >= a:
            money -= a
        return money


if __name__ == '__main__':
    pass
