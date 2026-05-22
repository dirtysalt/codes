#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    """
    @param str: the origin string
    @return: the start and end of every twitch words
    """

    def twitchWords(self, str):
        # Write your code here

        res = []
        if not str:
            return res
        idx = 0
        for i in range(1, len(str)):
            if str[i] != str[idx]:
                if (i - idx) >= 3:
                    res.append((idx, i - 1))
                idx = i
        if (len(str) - idx) >= 3:
            res.append((idx, len(str) - 1))
        return res
