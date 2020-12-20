#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """

        ans = 0
        for i in range(len(flowerbed)):
            if flowerbed[i] == 0:
                if (i > 0 and flowerbed[i - 1] == 1) or \
                        (i < (len(flowerbed) - 1) and flowerbed[i + 1] == 1):
                    pass
                else:
                    flowerbed[i] = 1
                    ans += 1
        return ans >= n


if __name__ == '__main__':
    sol = Solution()
    print(sol.canPlaceFlowers([1, 0, 0, 0, 1], 1))
    print(sol.canPlaceFlowers([1, 0, 0, 0, 0, 1], 2))
