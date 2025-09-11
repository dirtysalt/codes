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
    def findTarget(self, root: TreeNode, k: int) -> bool:
        from collections import Counter
        cnt = Counter()

        def collect(root):
            if not root:
                return
            cnt[root.val] += 1
            collect(root.left)
            collect(root.right)

        def fun(root):
            if not root:
                return False

            if root.val * 2 == k:
                if cnt[root.val] >= 2:
                    return True
            else:
                if cnt[k - root.val] != 0:
                    return True

            if fun(root.left):
                return True
            if fun(root.right):
                return True
            return False

        collect(root)
        ans = fun(root)
        return ans



