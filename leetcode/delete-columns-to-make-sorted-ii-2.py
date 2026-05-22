#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def minDeletionSize(self, A: List[str]) -> int:
        n = len(A)
        m = len(A[0])
        last = [''] * n
        ans = 0

        for i in range(m):
            tmp = [last[j] + A[j][i] for j in range(n)]
            # print(tmp)

            _delete = False
            _ascending = True

            for j in range(1, n):
                if tmp[j - 1] > tmp[j]:
                    _delete = True
                    break

                elif tmp[j] == tmp[j - 1]:
                    _ascending = False

            if _delete:
                ans += 1
                continue

            if _ascending:
                break

            last = tmp
        return ans


cases = [
    (["xc", "yb", "za"], 0),
    (["zyx", "wvu", "tsr"], 3),
    (["xc", "yb", "za"], 0),
    (["ca", "bb", "ac"], 1)
]

import aatest_helper

aatest_helper.run_test_cases(Solution().minDeletionSize, cases)
