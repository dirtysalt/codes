#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """

        def min_node(root):
            if not root: return None
            l = min_node(root.left)
            r = min_node(root.right)
            x = root
            if l and l.val < x.val: x = l
            if r and r.val < x.val: x = r
            return x

        def max_node(root):
            if not root: return None
            l = max_node(root.left)
            r = max_node(root.right)
            x = root
            if l and l.val > x.val: x = l
            if r and r.val > x.val: x = r
            return x

        def fx(root):
            if not root: return

            lmax = max_node(root.left)
            rmin = min_node(root.right)

            if lmax and rmin and lmax.val > rmin.val:
                lmax.val, rmin.val = rmin.val, lmax.val
            elif lmax and lmax.val > root.val:
                lmax.val, root.val = root.val, lmax.val
            elif rmin and rmin.val < root.val:
                rmin.val, root.val = root.val, rmin.val

            fx(root.left)
            fx(root.right)

        fx(root)
