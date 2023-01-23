#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def expandBinaryTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        from collections import deque
        dq = deque()
        ans = root
        dq.append(root)

        while dq:
            root = dq.popleft()
            l = root.left
            if l is not None:
                root.left = TreeNode(-1)
                root.left.left = l
                dq.append(l)

            r = root.right
            if r is not None:
                root.right = TreeNode(-1)
                root.right.right = r
                dq.append(r)

        return ans


if __name__ == '__main__':
    pass
