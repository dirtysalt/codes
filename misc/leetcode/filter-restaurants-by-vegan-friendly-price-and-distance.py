#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def filterRestaurants(self, restaurants: List[List[int]], veganFriendly: int,
                          maxPrice: int, maxDistance: int) -> List[int]:
        tmp = [(id, r) for (id, r, v, p, d) in restaurants
               if v >= veganFriendly and p <= maxPrice and d <= maxDistance]
        tmp.sort(key=lambda x: (x[1], x[0]), reverse=True)
        ans = [x[0] for x in tmp]
        return ans
