#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def beautifulPartitions(self, s: str, k: int, minLength: int) -> int:
        MOD = 10 ** 9 + 7
        if s[0] not in '2357': return 0
        if s[-1] in '2357': return 0

        n = len(s)
        ps = [0]
        for i in range(1, n):
            if s[i] in '2357' and s[i - 1] not in '2357':
                ps.append(i)
        ps.append(n)

        first = [-1] * n
        j = 0
        for i in range(len(ps)):
            while j < len(ps) and ps[j] - ps[i] < minLength: j += 1
            if j < len(ps):
                first[i] = j

        import functools
        @functools.cache
        def dfs(i, K):
            if i == len(ps) - 1:
                return 1 if K == k else 0
            if (K + len(ps) - i) < k:
                return 0
            if first[i] == -1: return 0

            ans = 0
            for j in range(first[i], len(ps)):
                ans += dfs(j, K + 1)
            return ans

        ans = dfs(0, 0)
        ans = ans % MOD
        return ans


true, false, null = True, False, None
cases = [
    ("23542185131", 3, 2, 3),
    ("23542185131", 3, 3, 1),
    ("3312958", 3, 1, 1)
]

import aatest_helper

aatest_helper.run_test_cases(Solution().beautifulPartitions, cases)

if __name__ == '__main__':
    pass
