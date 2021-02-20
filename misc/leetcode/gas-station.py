#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        ss = list(zip(gas, cost))
        net = [x[0] - x[1] for x in ss]
        seen = set()

        def ok(s):
            if s in seen or net[s] < 0: return False
            st = 0
            i = s
            while True:
                st += net[i]
                seen.add(i)
                i = (i + 1) % len(net)
                if st < 0: return False
                if i == s: return True

        for i in range(len(net)):
            if ok(i): return i
        return False
