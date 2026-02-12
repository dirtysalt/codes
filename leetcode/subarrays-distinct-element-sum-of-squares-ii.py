#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class RangeSumer:
    class Base:
        def __init__(self, n):
            self.values = [0] * n

        def update(self, i, j, delta):
            for k in range(i, j + 1):
                self.values[k] += delta

        def query(self, i, j):
            acc = 0
            for k in range(i, j + 1):
                acc += self.values[k]
            return acc

    def __init__(self, n):
        self.n = n
        sz = 1
        while sz < n:
            sz <<= 1
        self.sum = [0] * (sz << 1)
        self.lazy = [0] * (sz << 1)
        self.sz = sz
        self.base = RangeSumer.Base(n)
        self.debug = False

    def dump(self):
        sz = 1
        off = 1
        while sz <= self.sz:
            print(self.sum[off:off + sz], self.lazy[off:off + sz])
            off += sz
            sz = sz << 1

    def query_and_update(self, i, j, delta):
        def do(i, j, k, s, sz):

            if i <= s <= (s + sz - 1) <= j:
                res = self.sum[k]
                self.apply_lazy(k, sz, delta)
                return res

            self.push_down(k, sz)
            mid = s + sz // 2
            res = 0
            if i < mid:
                res += do(i, j, 2 * k, s, sz // 2)
            if j >= mid:
                res += do(i, j, 2 * k + 1, mid, sz // 2)

            self.sum[k] = self.sum[2 * k] + self.sum[2 * k + 1]
            return res

        ans = do(i, j, 1, 0, self.sz)
        if self.debug:
            exp = self.base.query(i, j)
            self.base.update(i, j, delta)
            print('query_and_update(%d, %d) = %d' % (i, j, ans))
            self.dump()

            if ans != exp:
                assert (ans == exp)
        return ans

    def push_down(self, k, sz):
        if self.lazy[k] and sz != 1:
            v = self.lazy[k]
            self.apply_lazy(2 * k, sz // 2, v)
            self.apply_lazy(2 * k + 1, sz // 2, v)
            self.lazy[k] = 0

    def apply_lazy(self, k, sz, delta):
        self.sum[k] += delta * sz
        self.lazy[k] += delta

    def query(self, i, j):
        return self.query_and_update(i, j, 0)

    def update(self, i, j, delta):
        self.query_and_update(i, j, delta)



class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        n = len(nums)
        prev = {}
        ans, acc = 0, 0
        MOD = 10 ** 9 + 7
        sumer = RangeSumer(n)
        # sumer.debug = True
        for i in range(n):
            p = prev.get(nums[i], -1)
            prev[nums[i]] = i
            delta = 2 * sumer.query_and_update(p + 1, i, 1) + (i - p)
            acc = (acc + delta) % MOD
            ans = (ans + acc) % MOD
        return ans % MOD


true, false, null = True, False, None
import aatest_helper

cases = [
    ([1, 2], 6,),
    ([1, 2, 1], 15),
    ([2, 2], 3),
    ([2, 2, 5], 12),
    ([2, 2, 5, 5], 22),
    ([2, 3, 2, 1, 2, 5, 3, 4, 5, 2], 629)
]

# cases += aatest_helper.read_cases_from_file('tmp.in', 2)

aatest_helper.run_test_cases(Solution().sumCounts, cases)

if __name__ == '__main__':
    pass
