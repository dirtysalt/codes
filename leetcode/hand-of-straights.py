#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt


class Solution:
    def isNStraightHand(self, hand, W):
        """
        :type hand: List[int]
        :type W: int
        :rtype: bool
        """
        t = len(hand) // W
        if t * W != len(hand):
            return False

        counter = dict()
        for w in hand:
            counter[w] = counter.get(w, 0) + 1

        for _ in range(t):
            keys = list(counter.keys())
            keys.sort()
            start = keys[0]
            for i in range(W):
                v = start + i
                if v not in counter:
                    return False
                c = counter[v]
                if c == 1:
                    del counter[v]
                else:
                    counter[v] = c - 1
        return True
