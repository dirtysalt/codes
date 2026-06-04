#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def preimageSizeFZF(self, K):
        """
        :type K: int
        :rtype: int
        """

        # f(n) = n * (1/5 + 1/5^2 + 1/5^3 ...+ 1/5^k)
        # and f(n) is monotonic increasing.

        def zeros(n):
            res = 0
            k = 5
            while k <= n:
                res += n // k
                k *= 5
            return res

        # find low bound.
        l, r = 0, 5 * (K + 1)
        while (l <= r):
            m = (l + r) // 2
            c = zeros(m)
            if (c < K):
                l = m + 1
            else:
                r = m - 1
        lb = l

        l, r = 0, 5 * (K + 1)
        while (l <= r):
            m = (l + r) // 2
            c = zeros(m)
            if (c > K):
                r = m - 1
            else:
                l = m + 1
        rb = r
        return (rb - lb + 1)


if __name__ == '__main__':
    s = Solution()
    for K in (0, 1, 2, 5, 10):
        print((s.preimageSizeFZF(K)))
