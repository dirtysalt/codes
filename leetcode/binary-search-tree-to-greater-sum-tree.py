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
    def bstToGst(self, root: TreeNode) -> TreeNode:
        def fn(root: TreeNode, pv):
            if root is None:
                return pv

            pv = fn(root.right, pv)            
            pv += root.val
            root.val = pv
            pv = fn(root.left, pv)
            return pv

        pv = fn(root, 0)
        return root


import aatest_helper

null = None
t = aatest_helper.list_to_tree(
    [4, 1, 6, 0, 2, 5, 7, null, null, null, 3, null, null, null, 8])

t = Solution().bstToGst(t)
print(aatest_helper.tree_to_list(t))
