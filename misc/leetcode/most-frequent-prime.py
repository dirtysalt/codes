#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


def is_prime(x):
    y = int(x ** 0.5) + 1
    for z in range(2, y + 1):
        if x % z == 0: return False
    return True


class Solution:
    def mostFrequentPrime(self, mat: List[List[int]]) -> int:
        n, m = len(mat), len(mat[0])
        from collections import Counter
        cnt = Counter()

        def walk(i, j, dx, dy):
            value = mat[i][j]
            while True:
                i, j = i + dx, j + dy
                if not (0 <= i < n and 0 <= j < m): break
                value = value * 10 + mat[i][j]
                cnt[value] += 1

        for i in range(n):
            for j in range(m):
                for dx in (-1, 0, 1):
                    for dy in (-1, 0, 1):
                        if dx == 0 and dy == 0: continue
                        walk(i, j, dx, dy)

        if not cnt: return -1
        ans, maxc = -1, 0
        for x, c in cnt.items():
            if is_prime(x):
                if c > maxc or (c == maxc and x > ans):
                    ans = x
                    maxc = c
        return ans


true, false, null = True, False, None
import aatest_helper

cases = [
    ([[1, 1], [9, 9], [1, 1]], 19),
    ([[9], [3]], -1),
    ([[7, 7, 2, 2, 6, 8], [7, 9, 6, 8, 9, 4], [8, 3, 3, 2, 5, 6]], 97)
]

aatest_helper.run_test_cases(Solution().mostFrequentPrime, cases)

if __name__ == '__main__':
    pass
