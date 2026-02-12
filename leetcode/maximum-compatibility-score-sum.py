#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def maxCompatibilitySum(self, students: List[List[int]], mentors: List[List[int]]) -> int:
        m = len(students)
        mul = [[0] * m for _ in range(m)]

        for i in range(m):
            for j in range(m):
                acc = 0
                for k in range(len(students[0])):
                    acc += students[i][k] == mentors[j][k]
                mul[i][j] = acc

        # print(mul)
        import functools

        @functools.lru_cache(maxsize=None)
        def search(x, st):
            if x == m:
                return 0

            ans = 0
            for i in range(m):
                if st & (1 << i):
                    continue
                ans = max(ans, mul[x][i] + search(x + 1, st | (1 << i)))
            return ans

        ans = search(0, 0)
        return ans


if __name__ == '__main__':
    pass
