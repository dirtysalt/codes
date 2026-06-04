#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def maxNumberOfAlloys(self, n: int, k: int, budget: int, composition: List[List[int]], stock: List[int],
                          cost: List[int]) -> int:

        def test(I, K):
            c = 0
            for i in range(n):
                need = K * composition[I][i]
                if need > stock[i]:
                    c += cost[i] * (need - stock[i])
                if c > budget:
                    return False
            return True

        ans = 0

        for i in range(k):
            s, e = 0, budget + max(stock)
            while s <= e:
                m = (s + e) // 2
                if test(i, m):
                    s = m + 1
                else:
                    e = m - 1
            ans = max(ans, e)
        return ans


if __name__ == '__main__':
    pass
