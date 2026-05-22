#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """

        xs = [0] * 10
        ys = [0] * 10
        A = 0
        B = 0
        for i in range(len(secret)):
            if secret[i] == guess[i]:
                A += 1
            else:
                xs[ord(secret[i]) - ord('0')] += 1
                ys[ord(guess[i]) - ord('0')] += 1

        for i in range(10):
            if ys[i] != 0:
                B += min(ys[i], xs[i])

        return '{}A{}B'.format(A, B)
