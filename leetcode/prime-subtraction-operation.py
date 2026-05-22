#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def primeSubOperation(self, nums: List[int]) -> bool:
        N = 1000
        P = [0] * (N + 1)
        for i in range(2, N + 1):
            if P[i] == 1: continue
            for j in range(2, N + 1):
                if i * j > N: break
                P[i * j] = 1

        PS = []
        for i in range(2, N + 1):
            if P[i] == 0:
                PS.append(i)

        def find(value):
            s, e = 0, len(PS) - 1
            while s <= e:
                m = (s + e) // 2
                if PS[m] <= value:
                    s = m + 1
                else:
                    e = m - 1
            return PS[e] if e >= 0 else -1

        last = 1
        for x in nums:
            # find y that (x - y) >= last
            # y <= x - last
            value = find(x - last)
            if value != -1:
                last = (x - value + 1)
            elif x >= last:
                last = x + 1
            else:
                return False
        return True


true, false, null = True, False, None
import aatest_helper

cases = [
    ([4, 9, 6, 10], true),
    ([6, 8, 11, 12], true),
    ([5, 8, 3], false),
    ([19, 10], true),
]

aatest_helper.run_test_cases(Solution().primeSubOperation, cases)

if __name__ == '__main__':
    pass
