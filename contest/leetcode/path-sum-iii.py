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
    def pathSum(self, root: TreeNode, sum: int) -> int:

        from collections import Counter
        ans = 0

        def visit(root):
            nonlocal ans
            c = Counter()
            if root is None:
                return Counter()

            lc = visit(root.left)
            rc = visit(root.right)
            v = root.val
            c = Counter()
            for x, c0 in lc.items():
                c[x + v] += c0
            for x, c0 in rc.items():
                c[x + v] += c0
            c[v] += 1

            ans += c[sum]
            return c

        visit(root)
        return ans
