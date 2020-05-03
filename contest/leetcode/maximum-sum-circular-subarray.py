#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def maxSubarraySumCircular(self, A: List[int]) -> int:
        if all((x < 0 for x in A)):
            return max(A)

        n = len(A)

        # 不考虑边界的基本情况
        ans = 0
        res = 0
        for v in A:
            res += v
            if res < 0:
                res = 0
            ans = max(res, ans)

        # 考虑边界的话, vec[i]表示A[:i+1]连续seq的最大值
        def build_max_vec(A):
            max_vec = [0] * n
            res = 0
            mv = 0
            for idx, v in enumerate(A):
                res += v
                mv = max(mv, res)
                max_vec[idx] = mv
            return max_vec

        vec_fwd = build_max_vec(A)
        vec_bwd = build_max_vec(reversed(A))
        for i in range(0, n-1):
            res = vec_fwd[i] + vec_bwd[n-i-2]
            ans = max(res, ans)
        return ans


import aatest_helper

cases = [
    ([1, -2, 3, -2], 3),
    ([3, -2, 2, -3], 3),
    ([3, -1, 2, -1], 4),
    ([5, -3, 5], 10),
    ([-2, -3, -1], -1),
]

aatest_helper.run_test_cases(Solution().maxSubarraySumCircular, cases)
