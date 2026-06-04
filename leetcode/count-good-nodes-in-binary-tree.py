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
    def goodNodes(self, root: TreeNode) -> int:
        ans = 0

        def visit(root, m):
            nonlocal ans
            if root is None:
                return

            if m <= root.val:
                ans += 1
            m = max(m, root.val)
            visit(root.left, m)
            visit(root.right, m)

        inf = 1 << 30
        visit(root, -inf)
        return ans
