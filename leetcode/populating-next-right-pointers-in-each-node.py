#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

# Definition for binary tree with next pointer.
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        st = []

        from collections import deque
        Q = deque()
        Q.append((root, 0))
        while len(Q):
            (t, d) = Q.popleft()
            if not t: continue

            while len(st) < (d + 1):
                st.append(None)
            if st[d] is not None:
                st[d].next = t
            st[d] = t

            Q.append((t.left, d + 1))
            Q.append((t.right, d + 1))
        for x in st:
            x.next = None
