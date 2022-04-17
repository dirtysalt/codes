#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def waysToBuyPensPencils(self, total: int, cost1: int, cost2: int) -> int:
        n = total // cost1
        ans = 0
        for i in range(n + 1):
            left = total - i * cost1
            right = left // cost2 + 1
            ans += right
        return ans


if __name__ == '__main__':
    pass
