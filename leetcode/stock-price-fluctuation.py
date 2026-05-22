#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from sortedcontainers import SortedSet


class StockPrice:

    def __init__(self):
        self.Prices = dict()
        self.MinMax = SortedSet()
        self.Ts = 0

    def update(self, timestamp: int, price: int) -> None:
        if timestamp in self.Prices:
            old = self.Prices[timestamp]
            self.MinMax.remove((old, timestamp))

        self.Prices[timestamp] = price
        self.MinMax.add((price, timestamp))
        self.Ts = max(self.Ts, timestamp)

    def current(self) -> int:
        return self.Prices[self.Ts]

    def maximum(self) -> int:
        p, t = self.MinMax[-1]
        return p

    def minimum(self) -> int:
        p, t = self.MinMax[0]
        return p


# Your StockPrice object will be instantiated and called as such:
# obj = StockPrice()
# obj.update(timestamp,price)
# param_2 = obj.current()
# param_3 = obj.maximum()
# param_4 = obj.minimum()

if __name__ == '__main__':
    pass
