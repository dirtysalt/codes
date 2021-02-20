#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# note(yan): 这个做法有点类似merkel tree.
class Solution:
    def findDuplicateSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: List[TreeNode]
        """

        from collections import defaultdict
        tid_alloc = defaultdict(int)
        added = set()

        res = []

        def walk(root):
            if root is None:
                return 0

            left_id = walk(root.left)
            right_id = walk(root.right)

            key = '{}.{}.{}'.format(root.val, left_id, right_id)
            if key not in tid_alloc:
                tid = len(tid_alloc) + 1
                tid_alloc[key] = tid
            else:
                tid = tid_alloc[key]
                if tid not in added:
                    res.append(root)
                added.add(tid)
            return tid

        walk(root)
        return res
