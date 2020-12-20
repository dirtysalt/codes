#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt
#
# class Solution(object):
#     def isInterleave(self, s1, s2, s3):
#         """
#         :type s1: str
#         :type s2: str
#         :type s3: str
#         :rtype: bool
#         """
#         n = len(s1)
#         m = len(s2)
#         if n + m != len(s3): return False
#
#         st = []
#         for i in range(0, (n + 1)):
#             st.append([False] * (m + 1))
#         st[0][0] = True
#         for i in range(1, m + 1):
#             st[0][i] = s2[:i] == s3[:i]
#         for i in range(1, n + 1):
#             st[i][0] = s1[:i] == s3[:i]
#
#         for i in range(1, n + 1):
#             for j in range(1, m + 1):
#                 st[i][j] = (st[i - 1][j] and s1[i - 1] == s3[i + j - 1]) or \
#                            (st[i][j - 1] and s2[j - 1] == s3[i + j - 1])
#
#         # for x in st:
#         #     print x
#         return st[n][m]

class Solution:
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """

        n = len(s1)
        m = len(s2)
        if n > m:
            n, m = m, n
            s1, s2 = s2, s1
        if (n + m) != len(s3):
            return False
        dp = [[0] * (n + 1) for _ in range(2)]
        now = 0
        dp[now][0] = 1
        for i in range(n + m):
            for j in range(n + 1):
                val = 0
                if (0 <= (j - 1) < n) and s1[j - 1] == s3[i]:
                    val = max(val, dp[now][j - 1])
                if (0 <= (i - j) < m) and s2[i - j] == s3[i]:
                    val = max(val, dp[now][j])
                dp[1 - now][j] = val
            now = 1 - now
        return bool(dp[now][n])


if __name__ == '__main__':
    s = Solution()
    print(s.isInterleave('aabcc', 'dbbca', 'aadbbcbcac'))
