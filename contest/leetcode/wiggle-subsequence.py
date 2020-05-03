#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


# class Solution:
#     def wiggleMaxLength(self, nums: List[int]) -> int:
#         n = len(nums)
#         if n == 0:
#             return 0
#
#         dp = [[1] * n, [1] * n]
#
#         for i in range(1, n):
#             for j in reversed(range(i)):
#                 if nums[j] > nums[i]:
#                     dp[1][i] = max(dp[1][i], dp[0][j] + 1)
#
#             for j in reversed(range(i)):
#                 if nums[j] < nums[i]:
#                     dp[0][i] = max(dp[0][i], dp[1][j] + 1)
#
#             # print(dp[0], dp[1])
#
#         ans = max(max(dp[0]), max(dp[1]))
#         return ans

# class Solution:
#     def wiggleMaxLength(self, nums: List[int]) -> int:
#         n = len(nums)
#         if n == 0:
#             return 0
#
#         pos_sizes = {}
#         neg_sizes = {}
#
#         pos_sizes[1] = nums[0]
#         neg_sizes[1] = nums[0]
#
#         for i in range(1, n):
#             max_neg_sz = 0
#             sizes = sorted(pos_sizes.keys(), reverse=True)
#             for sz in sizes:
#                 if pos_sizes[sz] > nums[i]:
#                     max_neg_sz = sz
#                     break
#
#             # TODO: update neg_sizes: max_neg_sz + 1, nums[i], with min
#
#             max_pos_sz = 0
#             sizes = sorted(neg_sizes.keys(), reverse=True)
#             for sz in sizes:
#                 if neg_sizes[sz] < nums[i]:
#                     max_pos_sz = sz
#                     break
#
#             # TODO: update pos_sizes: max_pos_sz + 1, nums[i], with max
#
#             max_neg_sz += 1
#             if max_neg_sz in neg_sizes:
#                 neg_sizes[max_neg_sz] = min(neg_sizes[max_neg_sz], nums[i])
#             else:
#                 neg_sizes[max_neg_sz] = nums[i]
#
#             max_pos_sz += 1
#             if max_pos_sz in pos_sizes:
#                 pos_sizes[max_pos_sz] = max(pos_sizes[max_pos_sz], nums[i])
#             else:
#                 pos_sizes[max_pos_sz] = nums[i]
#
#         ans = max(pos_sizes.keys())
#         ans = max(ans, max(neg_sizes.keys()))
#         return ans

# 贪心算法，始终保持pos, neg最大长度以及最大/最小值
# 如果pos的下一个值比当前最大值还大的话，那么可以放弃当前最大值，而使用下一个值，长度却可以保持不变

class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0

        neg_sz, neg_min = 1, nums[0]
        pos_sz, pos_max = 1, nums[0]

        for i in range(1, n):
            if nums[i] <= neg_min:
                neg_min = nums[i]
            else:
                psz, pve = neg_sz + 1, nums[i]
                if psz > pos_sz or (psz == pos_sz and pve > pos_max):
                    pos_sz = psz
                    pos_max = pve

            if nums[i] >= pos_max:
                pos_max = nums[i]
            else:
                nsz, nve = pos_sz + 1, nums[i]
                if nsz > neg_sz or (nsz == neg_sz and nve < neg_min):
                    neg_sz = nsz
                    neg_min = nve

        ans = max(pos_sz, neg_sz)
        return ans


cases = [
    ([1, 7, 4, 9, 2, 5], 6),
    ([1, 5, 2, 1], 3)
]

import aatest_helper

aatest_helper.run_test_cases(Solution().wiggleMaxLength, cases)
