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
    def countMatchingSubarrays(self, nums: List[int], pattern: List[int]) -> int:
        n, m = len(nums), len(pattern)
        P = [0] * (n - 1)
        for i in range(1, n):
            d = nums[i] - nums[i - 1]
            if d > 0: d = 1
            if d < 0: d = -1
            P[i - 1] = d

        kmp = KMP(pattern)
        pos = kmp.find_all(P)
        ans = len(pos)
        return ans


if __name__ == '__main__':
    pass
