#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


# class Solution:
#     def numFriendRequests(self, ages: List[int]) -> int:
#         N = 120
#         cnt = [0] * (N + 1)
#
#         for x in ages:
#             cnt[x] += 1
#
#         ans = 0
#         # 这里可以优化从15开始
#         for i in range(1, N + 1):
#             for j in reversed(range(1, i)):
#                 if j > (0.5 * i + 7):
#                     ans += cnt[j] * cnt[i]
#                 else:
#                     break
#
#             if i > (0.5 * i + 7):
#                 ans += cnt[i] * (cnt[i] - 1)
#         return ans

class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        N = 120
        cnt = [0] * (N + 1)

        for x in ages:
            cnt[x] += 1

        ans = 0
        for i in range(15, N + 1):
            if cnt[i] == 0: continue
            for j in reversed(range(15, i)):
                if j <= (0.5 * i + 7):
                    break
                ans += cnt[j] * cnt[i]
            ans += cnt[i] * (cnt[i] - 1)
        return ans
