#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt


MOD = 10 ** 9 + 7


def POW(a, b):
    ans = 1
    a = a % MOD
    while b:
        if b & 0x1:
            ans = ans * a
            ans = ans % MOD
        b = b >> 1
        a = (a * a) % MOD
    return ans


class Fancy:
    def __init__(self):
        self.array = []
        self.ops = []
        self.ops.append((-1, 0, 1, 1))

    def append(self, val: int) -> None:
        self.array.append(val)

    def addAll(self, inc: int) -> None:
        idx = len(self.array) - 1
        _, add, mul, _ = self.ops[-1]
        self.ops.append((idx, add + inc, mul, POW(mul, MOD - 2)))

    def multAll(self, m: int) -> None:
        idx = len(self.array) - 1
        _, add, mul, _ = self.ops[-1]
        self.ops.append((idx, add * m, (mul * m) % MOD, POW(mul * m, MOD - 2)))

    def getIndex(self, idx: int) -> int:
        if idx >= len(self.array):
            return -1

        s, e = 0, len(self.ops) - 1
        while s <= e:
            m = (s + e) // 2
            if self.ops[m][0] >= idx:
                e = m - 1
            else:
                s = m + 1

        # print(self.ops)
        # apply latest op
        # and cancel op self.ops[e]

        _, add1, mul1, div1 = self.ops[-1]
        _, add2, mul2, div2 = self.ops[e]
        val = self.array[idx]

        # mul = mul1 // mul2
        # add = add1 - add2 * mul
        # ans = val * mul + add

        mul = (mul1 * div2) % MOD
        add = add1 - add2 * mul
        ans = val * mul + add
        while ans < 0:
            ans += MOD
        return ans % MOD


# Your Fancy object will be instantiated and called as such:
# obj = Fancy()
# obj.append(val)
# obj.addAll(inc)
# obj.multAll(m)
# param_4 = obj.getIndex(idx)

null = None
cases = [
    (["Fancy", "append", "addAll", "append", "multAll", "getIndex", "addAll", "append", "multAll", "getIndex",
      "getIndex", "getIndex"],
     [[], [2], [3], [7], [2], [0], [3], [10], [2], [0], [1], [2]],
     [null, null, null, null, null, 10, null, null, null, 26, 34, 20]),

]

import aatest_helper

aatest_helper.run_simulation_cases(Fancy, cases)
