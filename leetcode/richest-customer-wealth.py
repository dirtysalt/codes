#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        n = len(accounts)
        ans = 0
        for i in range(n):
            ans = max(ans, sum(accounts[i]))
        return ans
