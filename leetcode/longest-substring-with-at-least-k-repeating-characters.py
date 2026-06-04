#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

# 大致思路就是从全串中找到不满足点，然后切成成为子问题不断求解。时间复杂度估计O(nlgn), 但是依然比较耗时
# 讨论区里面有遍历unique character 1-26，然后使用sliding window的方案，好像也是比较好的思路

# class Solution:
#     def longestSubstring(self, s: str, k: int) -> int:
#         from collections import Counter
#
#         if k == 1:
#             return len(s)
#
#         def fx(s):
#             # print('check {}'.format(s))
#             if len(s) < k:
#                 return 0
#
#             c = Counter()
#             for x in s:
#                 c[x] += 1
#
#             subs = []
#             j = 0
#             for i in range(len(s)):
#                 if c[s[i]] < k:
#                     subs.append((j, i - 1))
#                     j += 1
#             subs.append((j, len(s) - 1))
#
#             if len(subs) == 1 and subs == [(0, len(s) - 1)]:
#                 return len(s)
#
#             ans = 0
#             for (f, t) in subs:
#                 res = fx(s[f:t + 1])
#                 ans = max(ans, res)
#             return ans
#
#         ans = fx(s)
#         return ans
#

class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        s = [ord(x) - ord('a') for x in s]

        if k == 1:
            return len(s)

        stats = [[0] * 26 for _ in range(len(s))]
        stats[0][s[0]] += 1
        for i in range(1, len(s)):
            stats[i] = stats[i - 1][:]
            stats[i][s[i]] += 1

        def fx(start, end):
            if (end - start + 1) < k:
                return 0

            subs = []
            j = start
            for i in range(start, end + 1):
                c = stats[end][s[i]] - (stats[start - 1][s[i]] if start > 0 else 0)
                if c < k:
                    subs.append((j, i - 1))
                    j += 1
            subs.append((j, end))

            if len(subs) == 1 and subs[0] == (start, end):
                return (end - start + 1)

            ans = 0
            for (f, t) in subs:
                res = fx(f, t)
                ans = max(ans, res)
            return ans

        ans = fx(0, len(s) - 1)
        return ans


cases = [
    ("aaabb", 3, 3),
    ("ababbc", 2, 5),
    ("bbaaacbd", 3, 3),
    ("weitong", 2, 0),
    ("baaabcb", 3, 3),
    ("aacbbbdc", 2, 3)
]

import aatest_helper

aatest_helper.run_test_cases(Solution().longestSubstring, cases)
