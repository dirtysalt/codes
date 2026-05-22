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
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """

        assert (len(preorder) == len(inorder))

        def walk(po, io):
            assert len(po) == len(io)
            if len(po) == 0:
                return None
            val = po[0]
            split = io.index(val)
            root = TreeNode(val)
            root.left = walk(po[1:split + 1], io[0:split])
            root.right = walk(po[split + 1:], io[split + 1:])
            return root

        root = walk(preorder, inorder)
        return root
