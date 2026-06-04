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
    def countNodes(self, root: TreeNode) -> int:

        def visit(root):
            # ok, height, count, ans
            if root is None:
                return True, 0, 0, 0

            lok, lh, lc, lans = visit(root.left)
            rok, rh, rc, rans = visit(root.right)
            ans = lans + rans
            c = lc + rc + 1
            h = max(lh, rh) + 1

            ok = False
            if lok and rok and (lh == rh or (lh == (rh + 1))):
                ok = True
                ans += 1

            return ok, h, c, ans

        ok, h, c, ans = visit(root)
        return ans
