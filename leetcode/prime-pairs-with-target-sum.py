#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List
from collections import Counter, defaultdict, deque
from functools import lru_cache
import heapq


class Solution:
    def findPrimePairs(self, n: int) -> List[List[int]]:
        def sieve_of_eratosthenes(n):
            is_prime = [True] * (n + 1)
            is_prime[0] = is_prime[1] = False

            for i in range(2, int(n ** 0.5) + 1):
                if is_prime[i]:
                    for j in range(i * i, n + 1, i):
                        is_prime[j] = False
            return is_prime

        P = sieve_of_eratosthenes(n)

        ans = []
        for x in range(1, n // 2 + 1):
            y = n - x
            if P[x] and P[y]:
                ans.append((x, y))
        return ans


if __name__ == '__main__':
    pass
