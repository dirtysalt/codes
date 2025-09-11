#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


def iter_bit_positions_fast(n):
    """Yield positions of set bits using bit tricks."""
    while n:
        lsb = n & -n
        yield lsb.bit_length() - 1
        n &= n - 1  # 清除最低的1-bit


class Solution:
    def maxProfit(self, n: int, edges: List[List[int]], score: List[int]) -> int:
        back = [[] for _ in range(n)]
        for u, v in edges:
            back[v].append(u)

        back_st = [0] * n
        for i in range(n):
            for v in back[i]:
                back_st[i] |= (1 << v)

        import functools
        @functools.cache
        def cost_upper_bound(st):
            pos = 1 + st.bit_count()
            idx = []
            for i in iter_bit_positions_fast((1 << n) - 1 - st):
                idx.append(i)
            idx.sort(key=lambda x: score[x])
            res = 0
            for i, v in enumerate(idx):
                res += (pos + i) * score[v]
            return res

        @functools.cache
        def search(st):
            if st == ((1 << n) - 1):
                return 0

            pos = 1 + st.bit_count()
            cost = 0
            idx = []
            for i in iter_bit_positions_fast((1 << n) - 1 - st):
                if (back_st[i] & st) != back_st[i]: continue
                idx.append(i)

            for i, v in enumerate(idx):
                ub = cost_upper_bound(st | (1 << v))
                if cost >= (ub + pos * score[v]):
                    continue
                res = pos * score[v] + search(st | (1 << v))
                cost = max(cost, res)
            return cost

        ans = search(0)
        return ans


true, false, null = True, False, None
import aatest_helper

cases = [
    aatest_helper.OrderedDict(n=2, edges=[[0, 1]], score=[2, 3], res=8),
    aatest_helper.OrderedDict(n=3, edges=[[0, 1], [0, 2]], score=[1, 6, 3], res=25),
    aatest_helper.OrderedDict(n=22, edges=[],
                              score=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22],
                              res=3795),
    (5, [[1, 2], [0, 3], [1, 4], [2, 3], [1, 3]], [50913, 47946, 97391, 27488, 69147], 897632)
]

aatest_helper.run_test_cases(Solution().maxProfit, cases)

if __name__ == '__main__':
    pass
