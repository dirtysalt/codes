#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def mostFrequentIDs(self, nums: List[int], freq: List[int]) -> List[int]:
        n = max(nums) + 1
        c = 1
        while (1 << c) < n:
            c += 1
        n = (1 << c)

        tree = [0] * (2 * n)

        def update(i, x):
            idx = i + n
            tree[idx] += x
            while idx != 1:
                p = idx // 2
                tree[p] = max(tree[2 * p], tree[2 * p + 1])
                idx = p

        ans = []
        for i, x in zip(nums, freq):
            update(i, x)
            ans.append(tree[1])
        return ans


if __name__ == '__main__':
    pass
