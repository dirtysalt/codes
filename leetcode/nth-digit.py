#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    """
    @param n: a positive integer
    @return: the nth digit of the infinite integer sequence
    """

    def findNthDigit(self, n):
        # write your code here

        d = 1
        base = 9
        acc = 9
        pacc = 0

        while n > acc:
            pacc = acc
            d += 1
            base *= 10
            acc += d * base

        n = n - 1 - pacc
        value = (n // d) + (10 ** (d - 1))
        offset = n % d
        return int(str(value)[offset])


if __name__ == '__main__':
    s = Solution()
    print(s.findNthDigit(5))
    print(s.findNthDigit(9))
    print(s.findNthDigit(10))
    print(s.findNthDigit(11))
    print(s.findNthDigit(12))
    print(s.findNthDigit(189))
    print(s.findNthDigit(190))
