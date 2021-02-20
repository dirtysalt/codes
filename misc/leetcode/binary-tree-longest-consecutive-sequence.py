#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


class Solution:
    """
    @param root: the root of binary tree
    @return: the length of the longest consecutive sequence path
    """

    def longestConsecutive(self, root):
        # write your code here

        def walk(root):
            if root is None:
                return 0, None
            lh, lv = walk(root.left)
            rh, rv = walk(root.right)
            outh, outv = 1, root.val

            if lh > 0 and (root.val + 1) == lv:
                lh += 1
                lv = root.val
            if lh > outh:
                outh = lh
                outv = lv

            if rh > 0 and (root.val + 1) == rv:
                rh += 1
                rv = root.val
            if rh > outh:
                outh = rh
                outv = rv
            return outh, outv

        res, _ = walk(root)
        return res
