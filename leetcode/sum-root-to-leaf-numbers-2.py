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
    def sumNumbers(self, root: TreeNode) -> int:
        from collections import deque
        if not root:
            return 0

        ans = 0
        q = deque()
        q.append((0, root))
        while q:
            (pfx, t) = q.popleft()
            pfx = pfx * 10 + t.val
            if t.left is None and t.right is None:
                ans += pfx
            if t.left:
                q.append((pfx, t.left))
            if t.right:
                q.append((pfx, t.right))
        return ans
