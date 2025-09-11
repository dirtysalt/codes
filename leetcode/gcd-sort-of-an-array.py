#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


def make_primes(K):
    mask = [1] * (K + 1)

    for i in range(2, K + 1):
        if mask[i] == 0:
            continue
        for j in range(2, K + 1):
            if i * j > K:
                break
            mask[i * j] = 0

    primes = []
    for i in range(2, K + 1):
        if mask[i] == 1:
            primes.append(i)
    return primes


def issorted(nums):
    for i in range(1, len(nums)):
        if nums[i] < nums[i - 1]:
            return False
    return True


def sort_by_idxs(nums, idxs, tmps):
    for j in idxs:
        tmps.append(nums[j])
    idxs.sort()
    tmps.sort()
    for j in range(len(idxs)):
        nums[idxs[j]] = tmps[j]


class Solution:
    def gcdSort(self, nums: List[int]) -> bool:
        primes = make_primes(round(max(nums) ** 0.5) + 1)

        if issorted(nums):
            return True

        from collections import defaultdict
        groups = defaultdict(list)
        backs = [[] for _ in range(len(nums))]
        for i in range(len(nums)):
            x = nums[i]
            for p in primes:
                if x < p: break
                if x % p == 0:
                    while x % p == 0:
                        x = x // p
                    groups[p].append(i)
                    backs[i].append(p)
            if x != 1:
                groups[x].append(i)
                backs[i].append(x)

        maski = [0] * len(nums)
        maskp = set()

        def dfs(i, idxs):
            for p in backs[i]:
                if p in maskp: continue
                maskp.add(p)
                for j in groups[p]:
                    if maski[j]:
                        continue
                    maski[j] = 1
                    idxs.append(j)
                    dfs(j, idxs)

        idxs = []
        tmps = []
        for i in range(len(nums)):
            if maski[i] == 0:
                idxs.clear()
                tmps.clear()

                maski[i] = 1
                idxs.append(i)
                dfs(i, idxs)

                sort_by_idxs(nums, idxs, tmps)

        return issorted(nums)


true, false, null = True, False, None
cases = [
    ([7, 21, 3], true),
    ([5, 2, 6, 2], false),
    ([10, 5, 9, 3, 15], true),
]

import aatest_helper

aatest_helper.run_test_cases(Solution().gcdSort, cases)

if __name__ == '__main__':
    pass
