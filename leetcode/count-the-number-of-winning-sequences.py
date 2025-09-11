#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt


class Solution:
    def countWinningSequences(self, s: str) -> int:
        score = {
            'FE': 1,
            'EF': -1,
            'WF': 1,
            'FW': -1,
            'EW': 1,
            'WE': -1
        }

        import functools
        from collections import Counter

        @functools.lru_cache(None)
        def dfs(i, last):
            if i == len(s):
                return Counter({0: 1})

            dist = Counter()
            for c in 'FEW':
                if c == last: continue
                key = c + s[i]
                value = score.get(key, 0)
                d = dfs(i + 1, c)
                for k, v in d.items():
                    dist[k + value] += v
            return dist

        dist = dfs(0, '')
        ans = 0
        for k, v in dist.items():
            if k > 0:
                ans += v
        MOD = 10 ** 9 + 7
        return ans % MOD


true, false, null = True, False, None
import aatest_helper

cases = [
    ('FFF', 3),
    ("FWEFW", 18),
]

aatest_helper.run_test_cases(Solution().countWinningSequences, cases)

if __name__ == '__main__':
    pass
