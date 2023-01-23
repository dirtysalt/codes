#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

MIN_VALUE = -(1 << 31) - 1

MAX_VALUE = (1 << 31)


class Solution:
    # def _isValidBST(self, root):
    #     """
    #     :type root: TreeNode
    #     :rtype: bool
    #     """
    #
    #     def check(root):
    #         if not root:
    #             return True, MAX_VALUE, MIN_VALUE
    #
    #         ok0, min0, max0 = check(root.left)
    #         ok1, min1, max1 = check(root.right)
    #
    #         min2 = min(min0, root.val, min1)
    #         max2 = max(max1, root.val, max0)
    #
    #         if root.val <= max0 or root.val >= min1 or not ok0 or not ok1:
    #             return False, min2, max2
    #
    #         return True, min2, max2
    #
    #     ok, _, _ = check(root)
    #     return ok


    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        def check(root, min_value, max_value):
            if root is None:
                return True
            if root.val <= min_value or root.val >= max_value:
                return False
            if check(root.left, min_value, root.val) and check(root.right, root.val, max_value):
                return True
            return False

        return check(root, MIN_VALUE, MAX_VALUE)
