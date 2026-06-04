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
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        res = []

        def travel(root, d):
            if not root: return
            if len(res) < d:
                for i in range(len(res), d):
                    res.append([])
            if d % 2 == 1:
                res[d - 1].append(root.val)
            else:
                res[d - 1].insert(0, root.val)
            travel(root.left, d + 1)
            travel(root.right, d + 1)

        travel(root, 1)
        return res
