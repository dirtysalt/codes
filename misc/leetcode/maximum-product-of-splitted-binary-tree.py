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
    def maxProduct(self, root: TreeNode) -> int:

        def visit(root: TreeNode):
            if root is None:
                return 0
            a = visit(root.left)
            b = visit(root.right)
            root.sum = a + b + root.val
            return root.sum

        tt = visit(root)

        def cut(root: TreeNode):
            if root is None:
                return 0

            a = cut(root.left)
            b = cut(root.right)
            ans = max(a, b, (tt-root.sum) * root.sum)
            return ans

        ans = cut(root) % (10 ** 9 + 7)
        return ans


import aatest_helper
cases = [
    (aatest_helper.list_to_tree([1, 2, 3, 4, 5, 6]), 110),
    (aatest_helper.list_to_tree([2, 3, 9, 10, 7, 8, 6, 5, 4, 11, 1]), 1025)
]
aatest_helper.run_test_cases(Solution().maxProduct, cases)
