#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        m = len(rolls)
        exp = mean * (m + n) - sum(rolls)
        if exp > 6 * n or exp < n:
            return []
        avg = exp // n
        ans = [avg] * n
        exp = exp - avg * n
        for i in range(exp):
            ans[i] += 1
        return ans


if __name__ == '__main__':
    pass
