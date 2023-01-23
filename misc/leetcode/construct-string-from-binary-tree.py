#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def tree2str(self, t):
        """
        :type t: TreeNode
        :rtype: str
        """

        def fn(t):
            if t is None:
                return ''
            s = str(t.val)
            if t.left is None and t.right is None:
                return s
            s += '('
            s += fn(t.left)
            s += ')'
            if t.right is not None:
                s += '('
                s += fn(t.right)
                s += ')'
            return s

        return fn(t)
