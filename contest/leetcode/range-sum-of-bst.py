#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

# Definition for a binary tree node.
from leetcode import aatest_helper


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        def fn(root):
            if root is None:
                return 0
            ans = 0
            if root.val < L:
                ans += fn(root.right)
            elif root.val > R:
                ans += fn(root.left)
            else:
                ans += root.val
                ans += fn(root.right)
                ans += fn(root.left)
            return ans

        ans = fn(root)
        return ans


null = None
cases = [
    (aatest_helper.list_to_tree([10, 5, 15, 3, 7, null, 18]), 7, 15, 32),
    (aatest_helper.list_to_tree([10, 5, 15, 3, 7, 13, 18, 1, null, 6]), 6, 10, 23)
]

sol = Solution()
aatest_helper.run_test_cases(sol.rangeSumBST, cases)
