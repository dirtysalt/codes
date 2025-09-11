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
    def longestZigZag(self, root: TreeNode) -> int:
        dp = {}

        def f(lr, root):
            key = '{}.{}'.format(id(root), lr)
            if key in dp:
                return dp[key]

            ans = 0
            if lr == 0 and root.right:
                ans = 1 + f(1, root.right)
            if lr == 1 and root.left:
                ans = 1 + f(0, root.left)
            dp[key] = ans
            return ans

        def f2(root):
            ans = 0
            if root.left:
                ans = max(ans, f(0, root.left) + 1)
                ans = max(ans, f2(root.left))
            if root.right:
                ans = max(ans, f(1, root.right) + 1)
                ans = max(ans, f2(root.right))
            return ans

        ans = f2(root)
        return ans

