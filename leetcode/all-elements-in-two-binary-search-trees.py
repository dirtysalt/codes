#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


from typing import List


class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        def fn(t, out):
            if t is None:
                return
            fn(t.left, out)
            out.append(t.val)
            fn(t.right, out)

        out1, out2 = [], []
        fn(root1, out1)
        fn(root2, out2)
        ans = []
        i, j = 0, 0
        while i < len(out1) and j < len(out2):
            if out1[i] < out2[j]:
                ans.append(out1[i])
                i += 1
            else:
                ans.append(out2[j])
                j += 1
        ans.extend(out1[i:])
        ans.extend(out2[j:])
        return ans
