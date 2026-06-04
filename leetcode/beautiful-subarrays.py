#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    """
    @param nums: an integer list
    @param numOdds: an integer
    @return: return the number of beautiful subarrays
    """

    def BeautifulSubarrays(self, nums, numOdds):
        # write your code here

        tmp = []
        odd = 0
        for x in nums:
            if x % 2 == 1:
                odd += 1
            tmp.append(odd)

        def find(x, end):
            if x == 0:
                return -1

            s, e = 0, end
            while s <= e:
                m = (s + e) // 2
                if tmp[m] >= x:
                    e = m - 1
                else:
                    s = m + 1
            p = s
            return p

        ans = 0
        # print(tmp)
        for i in range(len(tmp)):
            k = tmp[i]
            if k < numOdds:
                continue

            exp1 = k - numOdds + 1
            p1 = find(exp1, i)
            if p1 > i:
                continue
            exp2 = k - numOdds
            p2 = find(exp2, i)
            if p2 > i:
                continue
            # print(i, k, p2, p1)
            res = p1 - p2
            ans += res
        return ans
