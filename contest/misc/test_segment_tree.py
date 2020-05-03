#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class SegmentTree:
    def __init__(self, sz):
        n = 1
        while n < sz:
            n = n * 2
        # 此时的n可以容纳叶子节点，但是我们还需要开辟树节点
        # 并且树节点从1开始标记
        self.arr = [0] * (2 * n)
        self.n = n

    def get(self, idx):
        return self.arr[idx + self.n]

    def update(self, idx, value):
        p = (idx + self.n)
        self.arr[p] = value
        p = p // 2
        while p >= 1:
            i, j = p * 2, p * 2 + 1
            self.arr[p] = max(self.arr[i], self.arr[j])
            p = p // 2

    def total_max(self):
        return self.arr[1]


st = SegmentTree(10)
for i in range(0, 10):
    st.update(i, 10 + i)
    print(st.total_max())
