#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def accountBalanceAfterPurchase(self, purchaseAmount: int) -> int:
        x = purchaseAmount // 10
        d0 = purchaseAmount - (x * 10)
        d1 = (x + 1) * 10 - purchaseAmount
        if d0 < d1:
            return 100 - (x * 10)
        else:
            return 100 - (x + 1) * 10


if __name__ == '__main__':
    pass
