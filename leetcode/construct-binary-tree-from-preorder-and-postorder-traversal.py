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
    def constructFromPrePost(self, pre: List[int], post: List[int]) -> TreeNode:

        def build(pre, post):
            if not pre:
                return None

            assert pre[0] == post[-1]
            val = pre[0]
            t = TreeNode(val)
            if len(pre) == 1:
                return t

            left = pre[1]
            sz = post.index(left) + 1
            left_pre = pre[1:1 + sz]
            left_post = post[:sz]
            right_pre = pre[1 + sz:]
            right_post = post[sz:-1]

            t.left = build(left_pre, left_post)
            t.right = build(right_pre, right_post)
            return t

        root = build(pre, post)
        return root
