#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

# 按照位置排序，计算每个位置到达target时间。
# 如果前面的车比后面车快的话，到达时间也是按照后面的车计算的

class Solution:
    def carFleet(self, target, position, speed):
        """
        :type target: int
        :type position: List[int]
        :type speed: List[int]
        :rtype: int
        """

        ps = list(zip(position, speed))
        ps.sort()
        times = [(target - x[0]) / x[1] for x in ps]
        max_t = 0
        res = 0
        for t in times[::-1]:
            if t > max_t:
                max_t = t
                res += 1
        return res
