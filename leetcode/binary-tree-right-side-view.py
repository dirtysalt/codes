#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        ans = []

        def f(root, d):
            if root is None:
                return

            if d >= len(ans):
                ans.append(root.val)
            else:
                ans[d] = root.val

            f(root.left, d + 1)
            f(root.right, d + 1)

        f(root, 0)
        return ans
