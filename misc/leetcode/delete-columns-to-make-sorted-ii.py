#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def minDeletionSize(self, A: List[str]) -> int:
        n, m = len(A), len(A[0])
        prev = [0] * n  # 假设最开始前缀是完全相同的，没有办法区分大小

        ans = 0
        for j in range(m):
            st = [0] * n
            delete = False  # 是否删除当前列
            for i in range(1, n):
                if prev[i]:  # 如果上一列已经确定
                    continue

                if A[i][j] > A[i - 1][j]:
                    st[i] = 1
                elif A[i][j] == A[i - 1][j]:
                    continue
                else:  # A[i][j] < A[i-1][j]
                    delete = True
                    break

            if delete:
                ans += 1
            else:
                ok = 0
                for i in range(n):  # 确定本轮哪些列已经可以得到结果
                    prev[i] = prev[i] | st[i]
                    ok += prev[i]
                # 快速返回
                if ok == (n - 1):
                    break
        return ans


cases = [
    (["xc", "yb", "za"], 0),
    (["zyx", "wvu", "tsr"], 3),
    (["xc", "yb", "za"], 0),
    (["ca", "bb", "ac"], 1)
]

import aatest_helper

aatest_helper.run_test_cases(Solution().minDeletionSize, cases)
