#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt


class Fancy:

    def __init__(self):
        self.array = []
        self.ops = []
        self.cache = {}

    def append(self, val: int) -> None:
        self.array.append(val)

    def addAll(self, inc: int) -> None:
        idx = len(self.array) - 1
        self.cache.clear()
        self.ops.append((idx, 0, inc))

    def multAll(self, m: int) -> None:
        idx = len(self.array) - 1
        self.cache.clear()
        self.ops.append((idx, 1, m))

    def getIndex(self, idx: int) -> int:
        if idx >= len(self.array):
            return -1
        MOD = 10 ** 9 + 7
        s, e = 0, len(self.ops) - 1
        while s <= e:
            m = (s + e) // 2
            if self.ops[m][0] >= idx:
                e = m - 1
            else:
                s = m + 1

        # starts with s
        if s in self.cache:
            add, mul = self.cache[s]
        else:
            add, mul = 0, 1
            for _, op, v in self.ops[s:]:
                if op == 0:
                    add += v
                else:
                    add *= v
                    mul *= v
            # print(add, mul)
            self.cache[s] = (add, mul)

        val = self.array[idx] * mul + add
        return val % MOD

# Your Fancy object will be instantiated and called as such:
# obj = Fancy()
# obj.append(val)
# obj.addAll(inc)
# obj.multAll(m)
# param_4 = obj.getIndex(idx)
