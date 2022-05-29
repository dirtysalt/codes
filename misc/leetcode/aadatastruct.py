#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class UnionFind:
    def __init__(self, values):
        r, c, = {}, {}
        for v in values:
            r[v], c[v] = v, 1
        self.r, self.c = r, c

    def size(self, a):
        ra = self.find(a)
        return self.c[ra]

    def find(self, a):
        if a not in self.r:
            self.r[a] = a
            self.c[a] = 1
            return a

        # find root.
        x = a
        while True:
            ra = self.r[x]
            if ra == x:
                break
            x = ra

        # compress path.
        x = a
        while x != ra:
            rx = self.r[x]
            self.r[x] = ra
            x = rx
        return ra

    def merge(self, a, b):
        ra, rb = self.find(a), self.find(b)
        if ra == rb:
            return
        ca, cb = self.c[ra], self.c[rb]
        if ca > cb:
            ca, cb, ra, rb = cb, ca, rb, ra
        self.r[ra] = rb
        self.c[rb] += ca


class StringHashBuilder:
    BASE = 13131
    MOD = 151217133020331712151
    # OFFSET = ord('a')
    OFFSET = 96

    def __init__(self, s):
        n = len(s)
        self.hash = [0] * (n + 1)
        self.base = [0] * (n + 1)
        self.base[0] = b = 1
        self.hash[0] = h = 0
        for i in range(n):
            h = (h * self.BASE + ord(s[i]) - self.OFFSET) % self.MOD
            b = (b * self.BASE) % self.MOD
            self.hash[i + 1] = h
            self.base[i + 1] = b

    def getHash(self, left, right):
        upper = self.hash[right]
        lower = (self.hash[left] * self.base[right - left]) % self.MOD
        return (upper - lower + self.MOD) % self.MOD


class PrefixSumTree:
    def __init__(self, arr):
        n = len(arr)
        self.tree = [0] * (n + 1)
        self.n = n
        for i in range(n):
            self.updateSum(i, arr[i])

    def getSum(self, index):
        t = 0
        index = index + 1
        while index > 0:
            t += self.tree[index]
            index -= index & (-index)
        return t

    def updateSum(self, index, val):
        index = index + 1
        while index <= self.n:
            self.tree[index] += val
            index += index & (-index)


class PrefixSumMaxTree:
    def __init__(self, arr):
        n = len(arr)
        t = 1
        while t < n:
            t = t * 2
        self.t = t
        self.n = n
        self.Max = [0] * (2 * t)
        self.Sum = [0] * (2 * t)
        for i in range(n):
            self.Sum[i + t] = arr[i]
            self.Max[i + t] = arr[i]
        for i in reversed(range(1, t)):
            self.refreshIndex(i)

    def refreshIndex(self, index):
        l, r = 2 * index, 2 * index + 1
        self.Sum[index] = self.Sum[l] + self.Sum[r]
        self.Max[index] = max(self.Max[l], self.Max[r])

    def updateValue(self, index, value):
        i = index + self.t
        self.Max[i] += value
        self.Sum[i] += value
        i = i // 2
        while i >= 1:
            self.refreshIndex(i)
            i = i // 2

    def prefixSum(self, end):
        def lookup(index, start, size):
            if (start + size - 1) <= end:
                return self.Sum[index]
            if start > end or size == 1: return 0
            l = 2 * index
            r = l + 1
            size = size // 2
            a = lookup(l, start, size)
            b = lookup(r, start + size, size)
            return a + b

        return lookup(1, 0, self.t)

    def firstFit(self, value):
        def lookup(index, start, size):
            if self.Max[index] < value: return -1
            if size == 1: return start
            size = size // 2
            l = 2 * index
            a = lookup(l, start, size)
            if a != -1: return a
            b = lookup(l + 1, start + size, size)
            return b

        return lookup(1, 0, self.t)


if __name__ == '__main__':
    pass
