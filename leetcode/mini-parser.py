#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
# class NestedInteger:
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class NestedInteger:
    pass


class Solution:
    def deserialize(self, s: str) -> NestedInteger:
        def parse_int(s, i):
            sign = 1
            if s[i] == '-':
                sign = -1
                i += 1

            v = 0
            while i < len(s) and s[i].isdigit():
                v = v * 10 + ord(s[i]) - ord('0')
                i += 1
            v = v * sign
            return NestedInteger(v), i

        def parse_list(s, i):
            assert s[i] == '['
            res = NestedInteger()
            i += 1
            while s[i] != ']':
                value, i = parse_value(s, i)
                if s[i] == ',':
                    i += 1
                res.add(value)
            i += 1
            return res, i

        def parse_value(s, i):
            if s[i] == '[':
                res, i = parse_list(s, i)
            else:
                res, i = parse_int(s, i)
            return res, i

        res, e = parse_value(s, 0)
        assert e == len(s)
        return res
