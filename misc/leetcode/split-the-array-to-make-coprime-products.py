#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt
from typing import List


def get_primes(M):
    P = [0] * (M + 1)
    for i in range(2, M + 1):
        if P[i] == 1: continue
        for j in range(2, M + 1):
            if i * j > M: break
            P[i * j] = 1

    primes = []
    for i in range(2, M + 1):
        if P[i] == 0:
            primes.append(i)

    return primes


class Solution:
    def findValidSplit(self, nums: List[int]) -> int:
        M = min(max(nums), 10 ** 3)
        primes = get_primes(M)

        class Factors:
            def __init__(self):
                from collections import Counter
                self.small = [0] * len(primes)
                self.large = Counter()

        def update_factor(A, B, x):
            for i in range(len(primes)):
                p = primes[i]
                if x % p == 0:
                    c = 0
                    while x % p == 0:
                        c += 1
                        x = x // p
                    A.small[i] += c
                    B.small[i] -= c
            if x != 1:
                A.large[x] += 1
                B.large[x] -= 1

        def check(A, B):
            for x, y in zip(A.small, B.small):
                if x != 0 and y != 0:
                    return False

            import itertools
            for k in itertools.chain(A.large.keys(), B.large.keys()):
                if A.large[k] != 0 and B.large[k] != 0:
                    return False
            return True

        A = Factors()
        B = Factors()
        for x in nums:
            update_factor(A, B, x)

        B = Factors()
        for i in range(len(nums) - 1):
            update_factor(B, A, nums[i])
            if check(A, B):
                return i

        return -1


class Solution:
    def findValidSplit(self, nums: List[int]) -> int:
        M = min(max(nums), 10 ** 3)
        primes = get_primes(M)
        left = {}
        right = [0] * (len(nums))

        def update(p, idx):
            if p not in left:
                pos = idx
                left[p] = idx
            else:
                pos = left[p]
            right[pos] = idx

        for idx, x in enumerate(nums):
            for p in primes:
                if x % p == 0:
                    while x % p == 0:
                        x = x // p
                    update(p, idx)
            if x > 1:
                update(x, idx)

        ans = 0
        for idx, r in enumerate(right):
            if idx > ans:
                return ans
            ans = max(ans, r)
        return -1

true, false, null = True, False, None
import aatest_helper

cases = [
    ([2, 3, 3], 0),
    ([4, 7, 8, 15, 3, 5], 2),
    ([4, 7, 15, 8, 3, 5], -1),
]
# cases += aatest_helper.read_cases_from_file('tmp.in', 2)
print(len(get_primes(10 ** 3)))

aatest_helper.run_test_cases(Solution().findValidSplit, cases)

if __name__ == '__main__':
    pass
