#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """

        def walk(root, p, q):
            if root is None:
                return None, 0

            c = 0
            if root == p or root == q:
                c += 1
            t0, c0 = walk(root.left, p, q)
            if c0 == 2:
                return t0, c0
            t1, c1 = walk(root.right, p, q)
            if c1 == 2:
                return t1, c1
            c += c0 + c1
            return root, c

        ans, _ = walk(root, p, q)
        return ans
