#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    """
    @param cost: The cost of each interviewer
    @return: The total cost of all the interviewers.
    """

    def TotalCost(self, cost):
        # write your code here
        cost.sort(key=lambda x: x[0] - x[1])
        n = len(cost)
        ans = 0
        for i in range(n // 2):
            ans += cost[i][0]
        for i in range(n // 2, n):
            ans += cost[i][1]
        return ans
