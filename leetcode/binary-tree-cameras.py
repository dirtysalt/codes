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
    def minCameraCover(self, root: TreeNode) -> int:
        dp = {}

        def test(root, me, parent):
            if root is None:
                return 0

            key = (root, me, parent)
            if key in dp: return dp[key]

            ans = 1 << 20
            for x in (0, 1):
                if root.left is None and x == 1: continue

                a = test(root.left, x, me)
                for y in (0, 1):
                    if root.right is None and y == 1: continue

                    b = test(root.right, y, me)

                    # x, y, me, parent.
                    if x + y + me + parent == 0:
                        continue

                    cost = a + b + me
                    ans = min(ans, cost)

            dp[key] = ans
            return ans

        a = test(root, 0, 0)
        b = test(root, 1, 0)
        return min(a, b)


import aatest_helper

null = None
cases = [
    (aatest_helper.list_to_tree([0, 0, null, 0, 0]), 1),
    (aatest_helper.list_to_tree([0, 0, null, 0, null, 0, null, null, 0]), 2),
]

import aatest_helper

aatest_helper.run_test_cases(Solution().minCameraCover, cases)
