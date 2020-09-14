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
    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
        dels = set(to_delete)
        ans = []

        def visit(root):
            if root is None:
                return None

            l = visit(root.left)
            r = visit(root.right)
            if root.val in dels:
                ans.append(l)
                ans.append(r)
                return None

            root.left = l
            root.right = r
            return root

        r = visit(root)
        ans.append(r)
        ans = [x for x in ans if x is not None]
        return ans
