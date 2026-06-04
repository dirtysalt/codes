#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        max_int = 1 << 31
        bits = [0] * 32
        for n in nums:
            n += max_int
            for i in range(32):
                if n & (1 << i):
                    bits[i] += 1
        v = 0
        for i in range(31, -1, -1):
            v = (v << 1) + (bits[i] % 3)
        return v - max_int


if __name__ == '__main__':
    s = Solution()
    print(s.singleNumber([1]))
    print(s.singleNumber([-2, -2, 1, 1, -3, 1, -3, -3, -4, -2]))
