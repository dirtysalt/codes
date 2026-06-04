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
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """

        res = []

        def walk(root, path):
            if root.left is None and root.right is None:
                path.append(root.val)
                res.append('->'.join([str(x) for x in path]))
                path.pop()
                return

            path.append(root.val)
            if root.left:
                walk(root.left, path)
            if root.right:
                walk(root.right, path)
            path.pop()

        if root:
            path = []
            walk(root, path)
        return res
