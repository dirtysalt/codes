#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

# class Solution(object):
#     def minDistance(self, word1, word2):
#         """
#         :type word1: str
#         :type word2: str
#         :rtype: int
#         """
#         word1 = '#' + word1
#         word2 = '#' + word2
#         n = len(word1)
#         m = len(word2)
#         st = []
#         for i in range(n):
#             st.append([0] * m)
#
#         st[0][0] = 0
#         for i in range(1, m):
#             st[0][i] = i
#         for i in range(1, n):
#             st[i][0] = i
#
#         for i in range(1, n):
#             for j in range(1, m):
#                 v = st[i - 1][j - 1] + (1 if word1[i] != word2[j] else 0)
#                 v = min(v, st[i - 1][j] + 1)
#                 v = min(v, st[i][j - 1] + 1)
#                 st[i][j] = v
#
#         return st[n - 1][m - 1]


class Solution:
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """

        n = len(word1)
        m = len(word2)
        if n < m:
            n, m = m, n
            word1, word2 = word2, word1

        print(word1, word2)
        dp = [[0] * (m + 1) for _ in range(2)]
        now = 0
        for i in range(m + 1):
            dp[now][i] = i

        for i in range(n):
            dp[1 - now][0] = dp[now][0] + 1

            for j in range(m):
                val = min(dp[1 - now][j], dp[now][j + 1]) + 1
                val = min(val, dp[now][j] + (0 if word1[i] == word2[j] else 1))
                dp[1 - now][j + 1] = val

            now = 1 - now
        return dp[now][m]


if __name__ == '__main__':
    sol = Solution()
    print(sol.minDistance('horse', 'ros'))
