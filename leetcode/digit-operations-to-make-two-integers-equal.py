#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt


class Solution:
    def minOperations(self, n: int, m: int) -> int:
        bits = 0
        while 10 ** bits <= n:
            bits += 1

        def get_primes(N):
            ps = []
            mask = [0] * (N + 1)
            for i in range(2, N + 1):
                if mask[i] == 1: continue
                for j in range(2, N + 1):
                    if i * j > N: break
                    mask[i * j] = 1
            for i in range(2, N + 1):
                if mask[i] == 0:
                    ps.append(i)
            return ps

        primes = set(get_primes(10 ** bits))

        def choose(x):
            d = [int(c) for c in str(x)]
            if len(d) < bits:
                d = [0] * (bits - len(d)) + d
            for i in range(len(d)):
                v = d[i]
                # keep bits same.
                if v > 1 or (v == 1 and i != 0):
                    d[i] = v - 1
                    yield int(''.join(str(c) for c in d))
                if v < 9:
                    d[i] = v + 1
                    yield int(''.join(str(c) for c in d))
                d[i] = v

        queue = []
        depth = [-1] * (10 ** bits)
        queue.append((n, n))
        if n in primes or m in primes:
            return -1

        import heapq
        while queue:
            (d, x) = heapq.heappop(queue)
            if depth[x] != -1: continue
            depth[x] = d
            if x == m:
                break
            for y in choose(x):
                if y in primes: continue
                if depth[y] != -1: continue
                # print(x, '---->', y)
                heapq.heappush(queue, (d + y, y))
        return depth[m]


true, false, null = True, False, None
import aatest_helper

cases = [
    (10, 12, 85),
    (4, 8, -1),
    (6, 2, -1),
    (15, 88, 490),
    (17, 72, -1),
    (36, 50, 353),
    (5637, 2034, 34943)
]

aatest_helper.run_test_cases(Solution().minOperations, cases)

if __name__ == '__main__':
    pass
