#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def minimumRefill(self, plants: List[int], capacityA: int, capacityB: int) -> int:
        n = len(plants)
        i, j = 0, n - 1
        ans = 0
        A, B = capacityA, capacityB
        while i <= j:
            if i == j:
                if A < plants[i] and B < plants[i]:
                    ans += 1
                break

            if A < plants[i]:
                ans += 1
                A = capacityA
            A -= plants[i]
            i += 1

            if B < plants[j]:
                ans += 1
                B = capacityB
            B -= plants[j]
            j -= 1
        return ans


if __name__ == '__main__':
    pass
