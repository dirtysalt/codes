#!/usr/bin/env python3
# coding:utf-8
# Copyright (C) dirlt

from typing import List
from collections import Counter, defaultdict, deque
from functools import lru_cache
import heapq

def makeprimes(n):
    p = [0] * (n + 1)
    sz = len(p)
    for i in range(2, sz):
        if i * i >= sz: break
        if p[i] == 1: continue
        for j in range(i, sz):
            if i * j >= sz: break
            p[i*j]=1
    return [x for x in range(2, sz) if p[x] == 0]

def gcd(x, y):
    while y:
        x, y = y, x % y
    return x

def findfactors(x, primes):
    factors = [1]
    for p in primes:
        if x < p: break
        if x % p == 0:
            rep = 0
            while x % p == 0:
                rep += 1
                x = x // p

            b = 1
            up = []
            for i in range(rep):
                b = b * p
                for ft in factors:
                    up.append(b * ft)
            factors.extend(up)

    return factors

class Solution:
    def countDifferentSubsequenceGCDs(self, nums: List[int]) -> int:
        maxn = max(nums)
        # 只需要查询sqrt(n)一下的素数
        primes = makeprimes(int(maxn ** 0.5) + 1)
        from collections import defaultdict
        ft = defaultdict(list)

        for x in nums:
            factors = findfactors(x, primes)
            # print(x, factors, x)
            # 注意这里并不是全部因子，全部因子需要包含x//f
            # 但是这里可以判断，如果rem <= max(factors)的话
            # 那么也没有必要包含进来
            # for f in factors:
            #     rem = x // f
            #     ft[f].append(rem)
            #     ft[rem].append(f)
            maxf = max(factors)
            for f in factors:
                rem = x // f
                ft[f].append(rem)
                if rem > maxf:
                    ft[rem].append(f)

        ans = 0
        # print(ft)
        for f, rs in ft.items():
            x = rs[0]
            for y in rs:
                x = gcd(x, y)
                if x == 1:
                    break
            if x == 1:
                ans += 1

        return ans

class Solution2:
    def countDifferentSubsequenceGCDs(self, nums: List[int]) -> int:
        maxn = max(nums)
        nums = set(nums)

        ans = 0
        for x in range(1, maxn + 1):
            if x in nums:
                # print(x)
                ans += 1
                continue

            g = None
            for y in range(x, maxn + 1, x):
                if y not in nums: continue
                if g is None:
                    g = y // x
                else:
                    g = gcd(g, y // x)
                if g == 1:
                    # print(x)
                    ans += 1
                    break

        return ans

cases = [
    ([6,10,3], 5),
    ([5,15,40,5,6], 7),
]

import aatest_helper
aatest_helper.run_test_cases(Solution().countDifferentSubsequenceGCDs, cases)
aatest_helper.run_test_cases(Solution2().countDifferentSubsequenceGCDs, cases)



if __name__ == '__main__':
    pass
