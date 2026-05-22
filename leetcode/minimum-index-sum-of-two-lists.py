#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """

        ans = len(list1) + len(list2)
        res = []
        for i in range(len(list1)):
            for j in range(len(list2)):
                if list1[i] == list2[j]:
                    index = i + j
                    if index <= ans:
                        if index < ans:
                            res.clear()
                            ans = index
                        res.append(list1[i])
        return res
