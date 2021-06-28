#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List
from collections import Counter, defaultdict, deque
from functools import lru_cache
import heapq


# class Solution:
#     def wonderfulSubstrings(self, word: str) -> int:
#         dp = [[0] * 1024 for _ in range(2)]
#         now = 0
#         ans = 0
#
#         # dp[i][st] # 截止到ith这个字符串上，以ith为结尾，各个state的分布情况
#         for i, w in enumerate(word):
#             t = ord(w) - ord('a')
#
#             for s in range(1024):
#                 dp[1 - now][s ^ (1 << t)] = dp[now][s]
#             dp[1 - now][1 << t] += 1
#
#             now = 1 - now
#             ans += dp[now][0]
#             for j in range(10):
#                 ans += dp[now][1 << j]
#         return ans

class Solution:
    def wonderfulSubstrings(self, word: str) -> int:
        from collections import Counter
        cnt = Counter()
        acc = 0
        ans = 0

        cnt[0] = 1
        for i, w in enumerate(word):
            t = ord(w) - ord('a')
            acc = acc ^ (1 << t)
            # xor([...i]) = acc
            # xor([..j]) = acc
            # then xor(j+1..i) = 0
            ans += cnt[acc]

            # xor([..i]) =acc
            # xor(..j]) = acc ^(1 << x)
            # then xor(j+1..) = (1<<x)
            for j in range(10):
                exp = acc ^ (1 << j)
                ans += cnt[exp]

            cnt[acc] += 1
        return ans


true, false, null = True, False, None
cases = [
    ("aba", 4),
    ("aabb", 9),
    ("he", 2),
    ("d", 1),
    ("fiabhedce", 9)
]

import aatest_helper

aatest_helper.run_test_cases(Solution().wonderfulSubstrings, cases)

if __name__ == '__main__':
    pass
