#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt
import bisect
import random


class Solution:

    def __init__(self, w):
        """
        :type w: List[int]
        """

        self.wsum = sum(w)
        ws = []
        acc = 0
        for x in w:
            acc += x
            ws.append(acc)
        self.ws = ws
        self.rnd = random.Random(42)

    def pickIndex(self):
        """
        :rtype: int
        """
        value = self.rnd.randint(1, self.wsum)
        return bisect.bisect_left(self.ws, value)

# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
