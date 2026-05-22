#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


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


class Solution:
    def canTraverseAllPairs(self, nums: List[int]) -> bool:
        # quick check.
        c = len([x for x in nums if x == 1])
        if c == 1 and len(nums) == 1:
            return True
        if c != 0: return False

        # compute primes
        nums = list(set(nums))
        N = int((10 ** 5) * 0.5) + 1
        N = min(max(nums), N)
        P = [0] * (N + 1)
        for i in range(2, N + 1):
            if P[i] == 1: continue
            for j in range(2, N + 1):
                if i * j > N: break
                P[i * j] = 1
        PS = []
        for i in range(2, N + 1):
            if P[i] == 0: PS.append(i)

        # decompose factors with cache
        import functools
        @functools.cache
        def decompose_factors(x):
            if x == 1: return []
            fs = []
            for p in PS:
                if x % p == 0:
                    while x % p == 0:
                        x = x // p
                    fs.append(p)
                    break

            if not fs:
                fs.append(x)
            else:
                fs.extend(decompose_factors(x))
            return fs

        n = len(nums)
        factors = []
        VALUES = set()
        for x in nums:
            fs = decompose_factors(x)
            factors.append(fs)
            VALUES.update(fs)

        # print(N, VALUES, factors)
        fu = UnionFind(values=VALUES)
        for i in range(n):
            fs = factors[i]
            for j in range(1, len(fs)):
                fu.merge(fs[0], fs[j])

        # check all of them have a single parent.
        parent = None
        for v in VALUES:
            p = fu.find(v)
            if parent is None:
                parent = p
                continue
            if p != parent:
                return False
        return True


true, false, null = True, False, None
import aatest_helper

cases = [
    ([2, 3, 6], true),
    ([3, 9, 5], false),
    ([4, 3, 12, 8], true),
    ([42, 40, 45, 42, 50, 33, 30, 45, 33, 45, 30, 36, 44, 1, 21, 10, 40, 42, 42], false),
    (
        [90, 66, 70, 91, 20, 90, 75, 77, 75, 42, 75, 70, 78, 91, 39, 60, 13, 30, 33, 65, 77, 91, 77, 77, 91, 78, 48, 42,
         63,
         42, 42, 84, 70, 30, 78, 99, 90, 77, 84, 90, 78, 90, 30, 80, 55, 42, 60, 30, 40, 65, 26, 84, 66, 42, 33, 84],
        true),
    ([50, 49, 15, 7, 14, 42, 33, 15, 5, 21, 44, 40], true),
    ([1], true),
    ([99991] * (10 ** 5), true),
    # ([10 ** 5] * (10 ** 5), true),
]

aatest_helper.run_test_cases(Solution().canTraverseAllPairs, cases)

if __name__ == '__main__':
    pass
