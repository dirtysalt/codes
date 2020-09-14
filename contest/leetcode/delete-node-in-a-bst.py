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
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:

        def do(root, key):
            if root is None:
                return root

            if root.val == key:
                if root.left is None and root.right is None:
                    return None

                if root.left is None or root.right is None:
                    return root.left or root.right

                r = root.right
                while r.left is not None:
                    r = r.left

                root.val = r.val
                root.right = do(root.right, r.val)

            elif root.val > key:
                root.left = do(root.left, key)

            else:
                root.right = do(root.right, key)

            return root

        root = do(root, key)
        return root
