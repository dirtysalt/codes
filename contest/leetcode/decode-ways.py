#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """

        # preprocess.
        if not s: return 0
        if not s.isdigit(): return 0

        st = [0] * (len(s) + 1)
        st[0] = 1

        for i in range(0, len(s)):
            res = 0
            v = int(s[i])
            if v >= 1 and v <= 26:
                res += st[i]

            if i > 0:
                v = int(s[i - 1: i + 1])
                if s[i - 1] != '0' and 1 <= v <= 26:
                    res += st[i - 1]

            st[i + 1] = res

        return st[len(s)]


if __name__ == '__main__':
    s = Solution()
    print(s.numDecodings('12'))
    print(s.numDecodings('27'))
