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
    def kthLargestPerfectSubtree(self, root: Optional[TreeNode], k: int) -> int:

        sizes = []

        def dfs(t: TreeNode):
            if t is None:
                return 0, False

            if t.left is None and t.right is None:
                sizes.append(1)
                return 1, True

            a, oa = dfs(t.left)
            b, ob = dfs(t.right)
            ok = False
            if oa and ob and a == b:
                ok = True
                sizes.append(a + b + 1)
            return a + b + 1, ok

        dfs(root)
        sizes.sort(reverse=True)
        # print(sizes)
        return sizes[k - 1] if (k - 1) < len(sizes) else -1


if __name__ == '__main__':
    pass
