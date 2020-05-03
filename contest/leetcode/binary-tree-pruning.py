#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt

# Definition for a binary tree node.
from leetcode.aatest_helper import list_to_tree, tree_to_list


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def pruneTree(self, root: TreeNode) -> TreeNode:

        def fx(root):
            if root is None:
                return 0

            lh = fx(root.left)
            rh = fx(root.right)
            if lh == 0:
                root.left = None
            if rh == 0:
                root.right = None
            return lh + rh + root.val

        val = fx(root)
        if val == 0:
            return None
        return root


def test():
    null = None
    cases = [
        ([1, null, 0, 0, 1], [1, null, 0, null, 1]),
        ([1, 0, 1, 0, 0, 0, 1], [1, null, 1, null, 1]),
        ([1, 1, 0, 1, 1, 0, 1, 0], [1, 1, 0, 1, 1, null, 1]),
    ]
    sol = Solution()
    ok = True
    for c in cases:
        (root, exp) = c
        res = tree_to_list(sol.pruneTree(list_to_tree(root)))
        if res != exp:
            print('case failed. {}, out = {}'.format(c, res))
            ok = False
    if ok:
        print('cases passed!!!')


if __name__ == '__main__':
    test()
