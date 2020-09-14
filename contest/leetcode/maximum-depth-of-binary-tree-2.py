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
    def maxDepth(self, root: TreeNode) -> int:
        ans = 0

        def dfs(root, d):
            nonlocal ans
            if root is None:
                ans = max(ans, d)
                return

            dfs(root.left, d + 1)
            dfs(root.right, d + 1)

        dfs(root, 0)
        return ans
