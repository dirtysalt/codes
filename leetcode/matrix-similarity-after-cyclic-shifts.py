#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List
from collections import Counter, defaultdict, deque
from functools import lru_cache
import heapq


class Solution:
    def areSimilar(self, mat: List[List[int]], k: int) -> bool:
        def right_shift(xs, k):
            m = len(xs)
            xs2 = [0] * m
            for i in range(m):
                xs2[(i + k) % m] = xs[i]
            return xs2

        def left_shift(xs, k):
            m = len(xs)
            xs2 = [0] * m
            for i in range(m):
                xs2[(i - k + m) % m] = xs[i]
            return xs2

        n, m = len(mat), len(mat[0])
        for i in range(n):
            xs = mat[i]
            if i % 2 == 0:
                xs2 = left_shift(xs, k)
                if xs2 != xs:
                    return False
            else:
                xs2 = right_shift(xs, k)
                if xs2 != xs:
                    return False

        return True


if __name__ == '__main__':
    pass
