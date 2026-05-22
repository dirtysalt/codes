#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class CustomStack:

    def __init__(self, maxSize: int):
        from collections import Counter
        self.st = []
        self.max_size = maxSize
        self.op = Counter()

    def push(self, x: int) -> None:
        if len(self.st) == self.max_size:
            return
        self.st.append(x)

    def pop(self) -> int:
        if not self.st:
            return -1

        idx = len(self.st)
        inc = self.op[idx]
        self.op[idx] = 0
        if idx > 1:
            self.op[idx - 1] += inc

        value = self.st.pop() + inc
        return value

    def increment(self, k: int, val: int) -> None:
        k = min(k, len(self.st))
        self.op[k] += val

# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)
