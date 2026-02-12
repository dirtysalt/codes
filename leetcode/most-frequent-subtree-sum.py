#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import defaultdict


class Solution:
    def findFrequentTreeSum(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """

        counter = defaultdict(int)

        def visit(root):
            if root is None:
                return 0
            res = root.val
            if root.left:
                c = visit(root.left)
                res += c
            if root.right:
                c = visit(root.right)
                res += c
            counter[res] += 1
            return res

        if root is None:
            return []

        visit(root)
        res = list(counter.items())
        res.sort(key=lambda x: -x[1])
        freq = res[0][1]
        res = [x[0] for x in res if x[1] == freq]
        return res
