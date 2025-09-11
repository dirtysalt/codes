#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

import numpy as np


# IX是构造出来的线段树

class RMQSegmentTree:
    def __init__(self, A):
        self.INF = float('inf')
        self.A = A
        n = 1
        while n < len(A):
            n = n * 2
        IX = [None] * (2 * n)
        self.IX = IX
        self.IN = n
        self._init_index()

    def _value(self, i):
        if i is None:
            return self.INF
        return self.A[i]

    def _init_index(self):
        for i in range(len(self.A)):
            self.IX[i + self.IN] = i

        for i in range(self.IN - 1, 0, -1):
            i0 = self.IX[2 * i]
            i1 = self.IX[2 * i + 1]
            v0 = self._value(i0)
            v1 = self._value(i1)
            self.IX[i] = i0 if v0 <= v1 else i1

    def _update_index(self, i):
        p = i // 2
        while p:
            i0 = self.IX[2 * p]
            i1 = self.IX[2 * p + 1]
            v0 = self._value(i0)
            v1 = self._value(i1)
            self.IX[p] = i0 if v0 <= v1 else i1
            p = p // 2

    def update(self, i, x):
        self.A[i] = x
        self._update_index(i + self.IN)

    def _query(self, i, start, span, left, right):
        if (start + span) <= left or start >= right:
            return None
        if start >= left and (start + span) <= right:
            return self.IX[i]
        i0 = self._query(i * 2, start, span // 2, left, right)
        i1 = self._query(i * 2 + 1, start + span // 2, span // 2, left, right)
        v0 = self._value(i0)
        v1 = self._value(i1)
        return i0 if v0 <= v1 else i1

    def query(self, left, right):
        # [left, right]
        ans = self._query(1, 0, self.IN, left, right + 1)
        return ans


def naive_query(A, left, right):
    return np.argmin(A[left:right + 1]) + left


def main():
    for size in (10, 16, 20, 32):
        A = np.random.rand(size)
        rmq = RMQSegmentTree(A)
        n = len(A)
        for left in range(n):
            for right in range(left + 1, n):
                for _ in range(10):
                    p = np.random.randint(left, right)
                    v = np.random.rand()
                    rmq.update(p, v)
                    x = naive_query(A, left, right)
                    y = rmq.query(left, right)
                    if x != y:
                        print('F')
        print('PASS ON SIZE = {}'.format(size))


def main2():
    A = [0, 1, 2, 3, 4, 5, 6, 7]
    rmq = RMQSegmentTree(A)
    print(rmq.IX)
    print(rmq.query(0, 4))


if __name__ == '__main__':
    main()
