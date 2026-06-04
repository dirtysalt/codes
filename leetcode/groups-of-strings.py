#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt


from collections import Counter
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
    def groupStrings(self, words: List[str]) -> List[int]:
        def value(w):
            st = 0
            for c in w:
                c2 = ord(c) - ord('a')
                st = st | (1 << c2)
            return st

        values = [value(w) for w in words]
        un = UnionFind(values)
        tmp = set(values)

        for st in values:
            for i in range(26):
                st2 = st ^ (1 << i)
                if st2 in tmp:
                    un.merge(st, st2)

            for i in range(26):
                if st & (1 << i):
                    st2 = (1 << 26) | (st ^ (1 << i))
                    un.merge(st, st2)

        d = Counter(un.find(st) for st in values)
        return [len(d), max(d.values())]


true, false, null = True, False, None
cases = [
    (["a", "b", "ab", "cde"], [2, 3]),
    (["a", "ab", "abc"], [1, 3]),
]

import aatest_helper

# cases.append(aatest_helper.read_case_from_file("/Users/dirlt/Downloads/x.txt", [11058, 4265]))
# cases.append(aatest_helper.read_case_from_file("/Users/dirlt/Downloads/y.txt", [487, 101]))

aatest_helper.run_test_cases(Solution().groupStrings, cases)

if __name__ == '__main__':
    pass
