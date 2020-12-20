#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

# Definition for a binary tree node.
from collections import Counter


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """

        if not root: return []
        cnt = Counter()

        def walk(root):
            if root is None:
                return
            cnt[root.val] += 1
            walk(root.left)
            walk(root.right)

        walk(root)
        max_occs = max(cnt.values())
        ans = [x for x in cnt.keys() if cnt[x] == max_occs]
        return ans
