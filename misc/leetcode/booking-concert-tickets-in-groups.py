#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt
from typing import List


class PrefixTree:
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


class BookMyShow:

    def __init__(self, n: int, m: int):
        rows = [m] * n
        self.tree = PrefixTree(rows)
        self.nm = n, m
        self.rows = rows
        self.free = 0

    def gather(self, k: int, maxRow: int) -> List[int]:
        row = self.tree.firstFit(k)
        if row > maxRow or row == -1: return []
        n, m = self.nm
        col = m - self.rows[row]
        self.rows[row] -= k
        self.tree.updateValue(row, -k)
        return [row, col]

    def scatter(self, k: int, maxRow: int) -> bool:
        n, m = self.nm
        t = self.tree.prefixSum(maxRow)
        if t < k: return False
        free = self.free
        while k:
            take = min(self.rows[free], k)
            self.rows[free] -= take
            k -= take
            self.tree.updateValue(free, -take)
            if self.rows[free] == 0:
                free += 1
        self.free = free
        return True

# Your BookMyShow object will be instantiated and called as such:
# obj = BookMyShow(n, m)
# param_1 = obj.gather(k,maxRow)
# param_2 = obj.scatter(k,maxRow)

true, false, null = True, False, None
cases = [
    (["BookMyShow", "gather", "gather", "scatter", "scatter"], [[2, 5], [4, 0], [2, 0], [5, 1], [5, 1]],
     [null, [0, 0], [], true, false]
     ),
    (
        ["BookMyShow", "gather", "gather", "gather", "gather", "gather", "gather", "gather", "scatter", "scatter",
         "gather",
         "gather", "gather", "gather", "gather", "scatter", "gather", "gather", "scatter", "gather", "scatter",
         "scatter",
         "scatter", "gather", "scatter"],
        [[25, 941], [34, 1], [296, 21], [927, 18], [695, 15], [830, 22], [638, 2], [169, 15], [623, 16], [268, 6],
         [160, 16], [342, 5], [22, 8], [187, 11], [332, 24], [589, 14], [87, 14], [581, 4], [334, 14], [322, 0],
         [511, 4],
         [1000, 3], [938, 9], [19, 5], [672, 5]],
        [null, [0, 0], [0, 34], [1, 0], [2, 0], [3, 0], [], [0, 330], true, true, [4, 78], [4, 238], [4, 580], [4, 602],
         [5, 0], true, [5, 769], [], true, [], false, false, true, [], false]),
]

import aatest_helper

aatest_helper.run_simulation_cases(BookMyShow, cases)

if __name__ == '__main__':
    pass
