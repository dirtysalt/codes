#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        n = len(s)

        st = []
        st.append([[]])

        pp = []
        for i in range(n):
            pp.append([0] * n)
        for i in range(n):
            pp[i][i] = 1
        for sz in range(2, n + 1):
            for i in range(0, n - sz + 1):
                j = i + sz - 1
                if s[i] != s[j]: continue
                pp[i][j] = pp[i + 1][j - 1] if (i + 1) <= (j - 1) else 1

        for i in range(n):
            # search palindrome backward.
            rs = []
            for j in range(0, i + 1):
                if not pp[j][i]: continue
                xs = st[j]
                rs.extend([x + [s[j: i + 1]] for x in xs])
            st.append(rs)

        return st[n]


if __name__ == '__main__':
    s = Solution()
    print(s.partition("aab"))
