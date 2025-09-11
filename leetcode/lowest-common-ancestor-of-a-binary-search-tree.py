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
        if p.val > q.val:
            p, q = q, p

        def walk(root, p, q):
            if root == p or root == q:
                return root
            if root.val > p.val and root.val < q.val:
                return root
            if root.val > q.val:
                return walk(root.left, p, q)
            else:
                return walk(root.right, p, q)

        ans = walk(root, p, q)
        return ans
