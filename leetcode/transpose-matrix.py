#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def transpose(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        return list(zip(*A))


if __name__ == '__main__':
    s = Solution()
    print(s.transpose([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
