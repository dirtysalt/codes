#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

class Solution:
    def printTree(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[str]]
        """

        res = []

        def height(root):
            if root is None:
                return 0
            lh = height(root.left)
            rh = height(root.right)
            return max(lh, rh) + 1

        def walk(root, ht, row, offset, ans):
            if root is None:
                return
            walk(root.left, ht - 1, row + 1, offset, ans)
            offset += (1 << (ht - 1)) - 1
            ans[row][offset] = root.val
            offset += 1
            walk(root.right, ht - 1, row + 1, offset, ans)

        ht = height(root)
        width = (1 << ht) - 1
        ans = [[""] * width for _ in range(ht)]
        walk(root, ht, 0, 0, ans)
        return ans
