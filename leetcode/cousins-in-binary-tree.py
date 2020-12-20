#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        st = []

        def visit(root, parent, d):
            if root is None:
                return

            if root.val == x or root.val == y:
                st.append((parent, d))
                return

            visit(root.left, root, d + 1)
            visit(root.right, root, d + 1)
            return

        visit(root, None, 0)
        # print(st)

        if len(st) < 2:
            return False

        if st[0][1] == st[1][1] and st[0][0] is not st[1][0]:
            return True

        return False
