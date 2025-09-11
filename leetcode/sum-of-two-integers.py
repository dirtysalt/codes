#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """

        while a:
            a, b = (a & b) << 1, a ^ b
        return b


if __name__ == '__main__':
    s = Solution()
    print((s.getSum(10, 20)))
    print((s.getSum(16, 32)))
    # print(s.getSum(-1, 1))
