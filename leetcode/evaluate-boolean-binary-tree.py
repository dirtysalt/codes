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
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        def eval(root):
            if root.val in (0, 1):
                return bool(root.val)
            a = eval(root.left)
            b = eval(root.right)
            if root.val == 2:
                return a or b
            else:
                return a and b

        return eval(root)


if __name__ == '__main__':
    pass
