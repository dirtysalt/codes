#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        res = [0]
        for i in range(n):
            res2 = []
            for x in res:
                res2.append((0 << i) + x)
            for x in reversed(res):
                res2.append((1 << i) + x)
            res = res2

        return res


if __name__ == '__main__':
    s = Solution()
    print(s.grayCode(4))
