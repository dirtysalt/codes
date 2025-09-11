#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

# class Solution:
#     def new21Game(self, N: int, K: int, W: int) -> float:
#         if K == 0: return 1.0
#         from collections import defaultdict
#         st = {0: 1.0}
#         iw = 1 / W
#
#         ans = 0.0
#         while st:
#             st2 = defaultdict(float)
#
#             for k, p in st.items():
#                 for w in range(1, W + 1):
#                     if (k + w) >= K:
#                         if (k + w) <= N:
#                             ans += p * iw
#                     else:
#                         st2[k + w] += p * iw
#
#             # st = {k: p for k, p in st2.items() if (p * iw) > 1e-10}
#             st = st2
#         return round(ans, 5)

# note(yan): dp[n] 表示无论取多少次，取到n的概率
# dp[n] = dp[n-1] * 1/w + dp[n-2] * 1/w + ...d[n-w] *1/w
# 但是(dp[n-1] + .. dp[n-w]) 可以使用sliding window来计算

class Solution:
    def new21Game(self, N: int, K: int, W: int) -> float:
        if K == 0 or (N - K) >= W:
            return 1.0

        dp = [0] * (N + 1)
        dp[0] = 1.0
        sw = 1.0

        for i in range(1, N + 1):
            dp[i] = 1 / W * sw
            if i < K:
                sw += dp[i]
            if i >= W:
                sw -= dp[i - W]

        ans = sum(dp[K:])
        return round(ans, 5)


cases = [
    (10, 1, 10, 1.0),
    (21, 17, 10, 0.73278),
    # (10000, 10000, 10000, 0.0001),
    (0, 0, 1, 1),
    (421, 400, 47, 0.71188)
]
import aatest_helper

aatest_helper.run_test_cases(Solution().new21Game, cases)
