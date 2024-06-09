#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def maximumLength(self, nums: List[int], k: int) -> int:
        mx = [[0] * 3 for _ in range(k + 1)]
        fx = {}

        for x in nums:
            if x not in fx:
                fx[x] = [0] * (k + 1)
            f = fx[x]

            for kk in range(k, -1, -1):
                f[kk] += 1
                if kk > 0:
                    m = mx[kk - 1]
                    f[kk] = max(f[kk], (m[1] if m[2] == x else m[0]) + 1)
                    # f[kk] = max(f[kk], m[0] + 1)

                # update m
                v = f[kk]
                m = mx[kk]
                if v > m[0]:
                    if m[2] == x:
                        m[0] = v
                    else:
                        m[0], m[1], m[2] = v, m[0], x
                elif v > m[1] and m[2] != x:
                    m[1] = v

            # print(mx)

        return mx[k][0]


true, false, null = True, False, None
import aatest_helper

cases = [
    ([1, 2, 1, 1, 3], 2, 4),
    ([1, 2, 3, 4, 5, 1], 0, 2),
]

aatest_helper.run_test_cases(Solution().maximumLength, cases)

if __name__ == '__main__':
    pass
