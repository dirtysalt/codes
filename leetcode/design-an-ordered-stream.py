#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class OrderedStream:

    def __init__(self, n: int):
        self.data = [None] * n
        self.ptr = 0

    def insert(self, id: int, value: str) -> List[str]:
        id -= 1
        data = self.data
        ptr = self.ptr

        data[id] = value
        ans = []
        if ptr == id:
            while ptr < len(data) and data[ptr] is not None:
                ans.append(data[ptr])
                ptr += 1
            self.ptr = ptr
        return ans

# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(id,value)
