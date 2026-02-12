#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class KMP:
    @staticmethod
    def build_max_match(t):
        n = len(t)
        match = [0] * n
        c = 0
        for i in range(1, n):
            v = t[i]
            while c and t[c] != v:
                c = match[c - 1]
            if t[c] == v:
                c += 1
            match[i] = c
        return match

    def __init__(self, t):
        self.t = t
        self.max_match = self.build_max_match(t)

    def search(self, s):
        match = self.max_match
        t = self.t
        c = 0
        for i, v in enumerate(s):
            while c and t[c] != v:
                c = match[c - 1]
            if t[c] == v:
                c += 1
            if c == len(t):
                return i - len(t) + 1
        return -1

    def find_all(self, s):
        match = self.max_match
        t = self.t
        c = 0
        pos = []
        for i, v in enumerate(s):
            while c and t[c] != v:
                c = match[c - 1]
            if t[c] == v:
                c += 1
            if c == len(t):
                pos.append(i - len(t) + 1)
                c = match[c - 1]
        return pos


class Solution:
    def countCells(self, grid: List[List[str]], pattern: str) -> int:
        m, n = len(grid), len(grid[0])

        def horizon_string():
            ans = ''
            for i in range(m):
                ans += ''.join(grid[i])
            return ans

        def vertical_string():
            ans = ''
            for i in range(n):
                for j in range(m):
                    ans += grid[j][i]
            return ans

        kmp = KMP(pattern)

        def build_positions(s):
            pos = set()
            lastp = -1
            for p in kmp.find_all(s):
                lastp = max(lastp, p)
                end = p + len(pattern)
                pos.update(list(range(lastp, end)))
                lastp = end
            return pos

        h = build_positions(horizon_string())
        v = build_positions(vertical_string())
        ans = 0
        for i in range(m):
            for j in range(n):
                if (i * n + j) in h and (j * m + i) in v:
                    ans += 1
        return ans


true, false, null = True, False, None
import aatest_helper

cases = []
cases = [
    ([["a", "a", "c", "c"], ["b", "b", "b", "c"], ["a", "a", "b", "a"], ["c", "a", "a", "c"], ["a", "a", "b", "a"]],
     "abaca", 1),
    ([["c", "a", "a", "a"], ["a", "a", "b", "a"], ["b", "b", "a", "a"], ["a", "a", "b", "a"]], "aba", 4),
    ([["a"]], "a", 1),
]
# cases += aatest_helper.read_cases_from_file('tmp.in', 3)

aatest_helper.run_test_cases(Solution().countCells, cases)

if __name__ == '__main__':
    pass
