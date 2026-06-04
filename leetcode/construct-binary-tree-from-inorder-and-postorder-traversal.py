#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """

        assert (len(postorder) == len(inorder))

        def walk(io, po):
            assert len(io) == len(po)
            if len(po) == 0:
                return None
            val = po[-1]
            split = io.index(val)
            root = TreeNode(val)
            root.left = walk(io[:split], po[:split])
            root.right = walk(io[split + 1:], po[split:-1])
            return root

        root = walk(inorder, postorder)
        return root
