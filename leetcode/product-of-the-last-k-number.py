#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class ProductOfNumbers:

    def __init__(self):
        self.arrays = [1]
        self.last_zero = -1

    def add(self, num: int) -> None:
        last = self.arrays[-1]
        v = last * num
        if v == 0:
            self.last_zero = len(self.arrays)
            v = 1
        self.arrays.append(v)

    def getProduct(self, k: int) -> int:
        # print(self.arrays, self.last_zero, k)
        p = len(self.arrays) - 1 - k
        if (p + 1) <= self.last_zero:
            return 0
        v = self.arrays[p]
        v2 = self.arrays[-1]
        return v2 // v


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)

import aatest_helper

null = None
cases = [
    (["ProductOfNumbers", "add", "add", "add", "add", "add", "getProduct", "getProduct", "getProduct", "add",
      "getProduct"],
     [[], [3], [0], [2], [5], [4], [2], [3], [4], [8], [2]], [null, null, null, null, null, null, 20, 40, 0, null, 32]
     )
]

aatest_helper.run_simulation_cases(ProductOfNumbers, cases)
