#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """

        def merge(t1, t2):
            if t1 is None or t2 is None:
                return t1 or t2
            left = merge(t1.left, t2.left)
            right = merge(t1.right, t2.right)
            t1.val += t2.val
            t1.left = left
            t1.right = right
            return t1

        return merge(t1, t2)
