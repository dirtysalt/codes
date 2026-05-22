#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:

        def make_dist():
            return [0] * 11

        ans = 0

        def visit(root):
            nonlocal ans

            if root is None:
                return make_dist()

            if root.left is None and root.right is None:
                dist = make_dist()
                dist[1] = 1
                return dist

            left_dist = visit(root.left)
            right_dist = visit(root.right)
            for i in range(1, 11):
                for j in range(1, 11):
                    if (i + j) > distance: continue
                    ans += left_dist[i] * right_dist[j]

            dist = make_dist()
            for i in range(1, 11):
                dist[i] += left_dist[i - 1]
                dist[i] += right_dist[i - 1]
            return dist

        visit(root)
        return ans
