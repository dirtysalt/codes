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
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        if not root: return []

        st = []
        res = []
        root.parent = None
        st.append((root, sum, 0))

        while st:
            (r, v, d) = st.pop()
            if not r:
                continue

            if r.left is None and r.right is None:
                if r.val == v:
                    t = r
                    path = []
                    while t:
                        path.append(t.val)
                        t = t.parent
                    res.append(path[::-1])
                continue

            if d == 0:
                st.append((r, v, d + 1))
                ln = r.left
                if ln: ln.parent = r
                st.append((ln, v - r.val, 0))

            elif d == 1:
                rn = r.right
                if rn: rn.parent = r
                st.append((rn, v - r.val, 0))

        return res
