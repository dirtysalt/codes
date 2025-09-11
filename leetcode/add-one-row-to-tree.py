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
    def addOneRow(self, root: TreeNode, v: int, d: int) -> TreeNode:
        def visit(root, depth):
            if root is None:
                return

            if depth == (d - 1):
                l, r = root.left, root.right
                a = TreeNode(v)
                a.left = l
                l = a
                b = TreeNode(v)
                b.right = r
                r = b
                root.left = l
                root.right = r
                return

            visit(root.left, depth + 1)
            visit(root.right, depth + 1)

        if d == 1:
            a = TreeNode(v)
            a.left = root
            root = a
        else:
            visit(root, 1)
        return root
