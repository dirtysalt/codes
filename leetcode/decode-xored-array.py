#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        ans = []
        ans.append(first)

        for x in encoded:
            val = x ^ first
            first = val
            ans.append(val)

        return ans
