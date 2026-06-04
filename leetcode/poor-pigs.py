#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

"""
https://leetcode.com/problems/poor-pigs/discuss/94266/another-explanation-and-solution

With 2 pigs, poison killing in 15 minutes, and having 60 minutes, we can find the poison in up to 25 buckets in the following way.
Arrange the buckets in a 5×5 square:

 1  2  3  4  5
 6  7  8  9 10
11 12 13 14 15
16 17 18 19 20
21 22 23 24 25
Now use one pig to find the row (make it drink from buckets 1, 2, 3, 4, 5, wait 15 minutes,
make it drink from buckets 6, 7, 8, 9, 10, wait 15 minutes, etc).
Use the second pig to find the column (make it drink 1, 6, 11, 16, 21, then 2, 7, 12, 17, 22, etc).

Having 60 minutes and tests taking 15 minutes means we can run four tests.
If the row pig dies in the third test, the poison is in the third row.
If the column pig doesn't die at all, the poison is in the fifth column
(this is why we can cover five rows/columns even though we can only run four tests).

With 3 pigs, we can similarly use a 5×5×5 cube instead of a 5×5 square and again use one pig to determine the coordinate of one dimension
(one pig drinks layers from top to bottom, one drinks layers from left to right, one drinks layers from front to back).
So 3 pigs can solve up to 125 buckets.
"""


class Solution(object):
    def poorPigs(self, buckets, minutesToDie, minutesToTest):
        """
        :type buckets: int
        :type minutesToDie: int
        :type minutesToTest: int
        :rtype: int
        """
        pigs = 0
        rounds = minutesToTest / minutesToDie
        while True:
            if (rounds + 1) ** pigs >= buckets:
                break
            pigs += 1
        return pigs


if __name__ == '__main__':
    s = Solution()
    print((s.poorPigs(1000, 15, 60)))
