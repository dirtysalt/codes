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
    def rob(self, root: TreeNode) -> int:
        def fn(root: TreeNode):
            # max value of (rob, !rob)
            if root is None:
                return 0, 0

            (x0, y0) = fn(root.left)
            (x1, y1) = fn(root.right)
            a = root.val + y0 + y1
            b = max(x0, y0) + max(x1, y1)
            return a, b

        a, b = fn(root)
        ans = max(a, b)
        return ans


import aatest_helper

null = None
cases = [
    (aatest_helper.list_to_tree([3, 2, 3, null, 3, null, 1]), 7)
]

aatest_helper.run_test_cases(Solution().rob, cases)
