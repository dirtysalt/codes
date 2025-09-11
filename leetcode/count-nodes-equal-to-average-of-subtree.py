#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:

        ans = [0]

        def visit(root):
            if root == None:
                return 0, 0

            a, b = visit(root.left)
            c, d = visit(root.right)
            x = a + c + root.val
            y = b + d + 1
            if x // y == root.val:
                ans[0] += 1
            return x, y

        visit(root)
        return ans[0]


if __name__ == '__main__':
    pass
