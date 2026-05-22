#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        def seq(arr):
            n = len(arr)
            now, L, T = 0, 0, 0
            for i in range(n):
                now += arr[i] - arr[0]
                T += arr[i]

            for i in range(n):
                pos = arr[i]
                yield pos, now

                if (i + 1) < n:
                    delta = arr[i + 1] - arr[i]
                    T -= arr[i]
                    now += delta * (i + 1) - (n - i - 1) * delta

        n = len(nums)
        ans = [0] * n
        from collections import defaultdict
        dl = defaultdict(list)
        for p, x in enumerate(nums):
            dl[x].append(p)

        for x, arr in dl.items():
            for p, v in seq(arr):
                ans[p] = v
        return ans


if __name__ == '__main__':
    pass
