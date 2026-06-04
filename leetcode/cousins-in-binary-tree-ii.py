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
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        total = []

        def visit(root, d):
            if root is None: return
            if d == len(total): total.append(0)
            total[d] += root.val
            visit(root.left, d + 1)
            visit(root.right, d + 1)

        visit(root, 0)

        # print(total)

        def change(root, d):
            l = root.left
            r = root.right
            if not l and not r: return

            v = l.val if l else 0
            v += r.val if r else 0
            v = total[d + 1] - v
            if l:
                l.val = v
                change(l, d + 1)
            if r:
                r.val = v
                change(r, d + 1)

        change(root, 0)
        root.val = 0

        return root


if __name__ == '__main__':
    pass
