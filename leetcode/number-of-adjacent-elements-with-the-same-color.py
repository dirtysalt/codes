#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def colorTheArray(self, n: int, queries: List[List[int]]) -> List[int]:
        C = [0] * n
        ans = []
        now = 0

        for (i, c) in queries:
            if C[i] != 0:
                if i >= 1 and C[i] == C[i - 1]:
                    now -= 1
                if (i + 1) < n and C[i] == C[i + 1]:
                    now -= 1
            C[i] = c
            if i >= 1 and C[i] == C[i - 1]:
                now += 1
            if (i + 1) < n and C[i] == C[i + 1]:
                now += 1
            ans.append(now)
        return ans


if __name__ == '__main__':
    pass
