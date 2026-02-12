#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def escapeGhosts(self, ghosts, target):
        """
        :type ghosts: List[List[int]]
        :type target: List[int]
        :rtype: bool
        """

        my = abs(target[0]) + abs(target[1])
        for g in ghosts:
            dist = abs(target[0] - g[0]) + abs(target[1] - g[1])
            if dist <= my:
                return False
        return True
