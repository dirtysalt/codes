#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    """
    @param L: A positive integer
    @param R: A positive integer
    @return:  the number of interesting subranges of [L,R]
    """

    def PalindromicRanges(self, L, R):
        # test

        def is_palindrome(s):
            s = str(s)
            return s == s[::-1]

        res = 0
        a, b = 0, 0
        for i in range(L, R + 1):
            ok = is_palindrome(i)
            if ok:
                res += b
                a, b = b, a + 1
            else:
                res += (a + 1)
                a += 1
        return res


if __name__ == '__main__':
    sol = Solution()
    for (a, b, exp) in ((1, 2, 1), (1, 7, 12), (87, 88, 1)):
        print(sol.PalindromicRanges(a, b), exp)
