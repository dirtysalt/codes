#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

# https://www.lintcode.com/problem/the-kth-subarray/description

class Solution:
    """
    @param a: an array
    @param k: the kth
    @return: return the kth subarray
    """

    def thekthSubarray(self, a, k):
        # wrrite your code here

        tmp = [0]
        for x in a:
            tmp.append(tmp[-1] + x)

        # print(tmp)
        def test(v):
            res = 0
            j = 0
            for i in range(len(tmp)):
                while j < len(tmp) and (tmp[j] - tmp[i]) <= v:
                    j += 1
                j -= 1
                sz = (j - i)
                res += sz
            return res

        end = sum(a)
        begin = min(a)
        s, e = begin, end
        while s <= e:
            m = (s + e) // 2
            rank = test(m)
            # print(m, rank)
            if rank >= k:
                e = m - 1
            else:
                s = m + 1
        ans = s
        return ans
