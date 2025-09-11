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
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        ans = []

        def walk(root, d):
            if not root: return
            if d == len(ans):
                ans.append(0)
            ans[d] += root.val
            walk(root.left, d + 1)
            walk(root.right, d + 1)

        walk(root, 0)
        ans.sort(key=lambda x: -x)
        if (k - 1) < len(ans):
            return ans[k - 1]
        return -1


if __name__ == '__main__':
    pass
