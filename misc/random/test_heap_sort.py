#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt


class Heap:
    def __init__(self, cap):
        self.data = [None]
        self.cap = cap

    def adjust1(self, idx):
        c0 = 2 * idx
        c1 = 2 * idx + 1
        n = len(self.data)

        swap = None
        if c1 < n and self.data[c1] < self.data[idx]:
            if self.data[c0] < self.data[c1]:
                swap = c0
            else:
                swap = c1
        elif c0 < n and self.data[c0] < self.data[idx]:
            swap = c0

        if swap:
            n0, n1 = self.data[swap], self.data[idx]
            self.data[swap], self.data[idx] = n1, n0

        return swap

    def adjust(self, idx):
        n = len(self.data)
        p = idx
        while p < n:
            swap = self.adjust1(p)
            if swap is None:
                break
            p = swap
        p = idx // 2
        while p:
            swap = self.adjust1(p)
            if swap is None:
                break
            p = p // 2

    def append(self, value):
        evicted = None
        n = len(self.data)
        if (n - 1) == self.cap:
            evicted = self.data[1]
            self.data[1] = value
            self.adjust(1)
        else:
            self.data.append(value)
            self.adjust(n)
        return evicted

    def values(self):
        return self.data[1:]


if __name__ == '__main__':
    heap = Heap(10)
    for i in range(10):
        heap.append(i)
    print(heap.values())
    for i in range(10):
        ev = heap.append(i + 10)
        print(ev, heap.values())
