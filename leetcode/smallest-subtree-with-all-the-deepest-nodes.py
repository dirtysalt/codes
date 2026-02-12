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
    def subtreeWithAllDeepest(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """

        def solve(root, depth):
            # print(root, depth)

            if root.left and root.right:
                l, ld = solve(root.left, depth + 1)
                r, rd = solve(root.right, depth + 1)
                # print(root.val, l.val, r.val, ld, rd)
                if ld == rd:
                    res = root, ld
                elif ld > rd:
                    res = l, ld
                else:
                    res = r, rd

            elif root.left:
                l, ld = solve(root.left, depth + 1)
                res = l, ld

            elif root.right:
                r, rd = solve(root.right, depth + 1)
                res = r, rd

            else:
                res = root, depth

            return res

        if root is None: return None
        h, _ = solve(root, 1)
        return h
