#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isEvenOddTree(self, root: TreeNode) -> bool:
        last = {}

        def visit(root, d):
            if root is None: return True
            if d % 2 == 0:
                if root.val % 2 == 0: return False
                if d in last and root.val <= last[d]: return False
            else:
                if root.val % 2 == 1: return False
                if d in last and root.val >= last[d]: return False
            last[d] = root.val
            if not visit(root.left, d + 1): return False
            if not visit(root.right, d + 1): return False
            return True

        ans = visit(root, 0)
        return ans
