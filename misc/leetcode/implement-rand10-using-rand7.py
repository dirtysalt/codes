#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

# The rand7() API is already defined for you.
# def rand7():
# @return a random integer in the range 1 to 7


def rand7():
    return 1


class Solution(object):
    def rand10(self):
        """
        :rtype: int
        """

        base_rnd = None
        while True:
            base_rnd = rand7()
            if base_rnd <= 5:
                break

        ext_rnd = None
        while True:
            ext_rnd = rand7()
            if ext_rnd <= 6:
                break

        res = base_rnd
        if ext_rnd % 2 == 0:
            res += 5
        return res