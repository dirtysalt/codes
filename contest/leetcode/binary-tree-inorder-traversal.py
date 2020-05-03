#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """

        st = []
        res = []
        st.append((root, 0))

        while st:
            (n, d) = st.pop()
            if n is None: continue
            if d == 0:
                st.append((n, 1))
                st.append((n.left, 0))
            elif d == 1:
                res.append(n.val)
                st.append((n.right, 0))
        return res
