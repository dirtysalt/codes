#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

import heapq


class Solution:
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """

        xs = [1]
        ys = []
        while len(xs) < n:
            x = xs[-1]
            for i in (2, 3, 5):
                heapq.heappush(ys, x * i)
            while ys[0] == x:
                heapq.heappop(ys)
            y = ys[0]
            heapq.heappop(ys)
            xs.append(y)
        ans = xs[-1]
        return ans


if __name__ == '__main__':
    s = Solution()
    print((s.nthUglyNumber(2)))
    print((s.nthUglyNumber(10)))
    print((s.nthUglyNumber(1690)))
