#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def minSupplyStationNumber(self, root: Optional[TreeNode]) -> int:

        import functools
        @functools.cache
        def search(root, me, p):
            if root is None:
                return 0

            ans = 10000
            lr = ((0, 0), (0, 1), (1, 0), (1, 1))

            def bad(l, r):
                if (l, r, me, p) == (0, 0, 0, 0):
                    return True
                if l and root.left is None:
                    return True
                if r and root.right is None:
                    return True
                return False

            for l, r in lr:
                if bad(l, r): continue
                a = search(root.left, l, me) + l
                b = search(root.right, r, me) + r
                ans = min(ans, a + b)
            return ans

        ans = search(root, 1, 0) + 1
        if root.left or root.right:
            a = search(root, 0, 0)
            ans = min(ans, a)
        return ans


if __name__ == '__main__':
    pass
