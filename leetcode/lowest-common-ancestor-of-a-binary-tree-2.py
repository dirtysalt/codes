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
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def find_path(root, x, path):
            if not root:
                return False

            path.append(root)
            if root is x:
                return True
            ok = find_path(root.left, x, path) or find_path(root.right, x, path)
            if not ok:
                path.pop()
            return ok

        pa = []
        pb = []
        find_path(root, p, pa)
        find_path(root, q, pb)
        index = {}
        for p in pa:
            index[p.val] = p
        for p in reversed(pb):
            if p.val in index:
                return index[p.val]
        return None
