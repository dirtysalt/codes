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
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        nodes = []

        def f(root, x, y):
            if root is None:
                return
            nodes.append((x, y, root.val))
            f(root.left, x - 1, y + 1)
            f(root.right, x + 1, y + 1)

        f(root, 0, 0)
        nodes.sort()

        ans = []
        tmp = []
        px = None
        for (x, y, val) in nodes:
            if x != px:
                if tmp:
                    ans.append(tmp)
                    tmp = []
                px = x
            tmp.append(val)

        if tmp:
            ans.append(tmp)
        return ans
