#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, K: int) -> List[int]:

        ans = []

        def search(root, path):
            if root is None:
                return False

            path.append(root)
            if root is target:
                if K == 0:
                    ans.append(root.val)
                    return True

                # search root subnodes.
                fun(root, 0)
                # search parent nodes.
                # print(path)
                d = 1
                for i in reversed(range(len(path) - 1)):
                    x, y = path[i], path[i + 1]
                    if d == K:
                        ans.append(x.val)
                        break
                    if x.left is y:
                        fun(x.right, d + 1)
                    elif x.right is y:
                        fun(x.left, d + 1)
                    else:
                        assert False
                    d += 1
                return True

            if search(root.left, path):
                return True
            if search(root.right, path):
                return True
            path.pop()
            return False

        def fun(root, d):
            if root is None:
                return

            if d == K:
                ans.append(root.val)
                return

            fun(root.left, d + 1)
            fun(root.right, d + 1)

        path = []
        search(root, path)
        return ans
