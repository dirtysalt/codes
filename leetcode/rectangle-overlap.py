#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def isRectangleOverlap(self, rec1, rec2):
        """
        :type rec1: List[int]
        :type rec2: List[int]
        :rtype: bool
        """

        p1 = (rec1[0], rec1[1])
        p2 = (rec1[2], rec1[3])
        p3 = (rec2[0], rec2[1])
        p4 = (rec2[2], rec2[3])

        if (p1[1] >= p4[1]) or (p2[1] <= p3[1]) or (p3[0] >= p2[0]) or (p4[0] <= p1[0]):
            return False
        return True
