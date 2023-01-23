#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from aatest_helper import run_simulation_cases


class StockSpanner:

    def __init__(self):
        self.past = []

    def next(self, price: int) -> int:
        nc = 1
        while self.past:
            (v, c) = self.past.pop()
            if price >= v:
                nc += c
            else:
                self.past.append((v, c))
                break
        self.past.append((price, nc))
        return nc


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)

null = None
cases = [
    (["StockSpanner", "next", "next", "next", "next", "next", "next", "next"],
     [[], [100], [80], [60], [70], [60], [75], [85]], [null, 1, 1, 1, 2, 1, 4, 6])
]

run_simulation_cases(StockSpanner, cases)
