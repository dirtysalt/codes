#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def findLUSlength(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: int
        """

        n = len(a)
        m = len(b)
        if n == m and a == b:
            return -1
        return max(n, m)


if __name__ == '__main__':
    sol = Solution()
    print(sol.findLUSlength('aba', 'cdc'))
    print(sol.findLUSlength('abc', 'cdc'))
    print(sol.findLUSlength('aaa', 'aaa'))
    print(sol.findLUSlength("aefawfawfawfaw", "aefawfeawfwafwaef"))
    print(sol.findLUSlength('aaa', 'a'))
