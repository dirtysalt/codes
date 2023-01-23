#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        idx = 0
        if ruleKey == 'color':
            idx = 1
        elif ruleKey == 'name':
            idx = 2

        ans = 0
        for x in items:
            if x[idx] == ruleValue:
                ans += 1
        return ans
