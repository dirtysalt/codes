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
    def distributeCoins(self, root: TreeNode) -> int:
        ans = 0

        def pre(root: TreeNode):
            if root is None:
                return 0, 0

            lc, lv = pre(root.left)
            rc, rv = pre(root.right)
            return lc + rc + 1, lv + rv + root.val

        count, total = pre(root)
        if total % count != 0:
            return -1
        avg = total // count

        def visit(root):
            nonlocal ans
            if root is None:
                return 0, 0

            lc, lv = visit(root.left)
            rc, rv = visit(root.right)
            c = lc + rc + 1
            v = lv + rv + root.val
            if v != c * avg:
                delta = abs(v - c * avg)
                ans += delta
            return c, v

        visit(root)
        return ans
