#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Heap:
    def __init__(self, n):
        sz = 1
        while sz < n:
            sz = sz * 2
        self.sz = sz
        self.data = [(1 << 30)] * (2 * sz)

    def update(self, i, v):
        p = i + self.sz
        self.data[p] = v
        p = p // 2
        while p >= 1:
            x, y = 2 * p, 2 * p + 1
            self.data[p] = min(self.data[x], self.data[y])
            p = p // 2

    def top(self):
        return self.data[1]


class Solution:
    def shortestSubarray(self, A: List[int], K: int) -> int:

        def test(sz):
            heap = Heap(sz)
            acc = 0
            ans = 0
            for i in range(len(A)):
                # 这个性质非常好，每次只需要更新就行
                heap.update(i % sz, acc)
                acc += A[i]
                ans = max(ans, acc - heap.top())
            return ans >= K, ans

        s, e = 1, len(A)
        while s <= e:
            # print(s, e)
            sz = (s + e) // 2
            ok, ans = test(sz)
            # print(sz, ans, ok)
            if ok:
                e = sz - 1
            else:
                s = sz + 1
        ans = s
        if ans == (len(A) + 1):
            ans = -1
        return ans
