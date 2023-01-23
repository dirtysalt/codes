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
    def closeLampInTree(self, root: TreeNode) -> int:

        import functools
        @functools.cache
        def find(tree: TreeNode, flipNow: int, flipAll: int):
            if tree is None:
                return 0
            val = tree.val
            if flipNow:
                val = 1 - val
            if flipAll:
                val = 1 - val

            ts = []
            if val == 1:
                # C1.
                if True:
                    a = find(tree.left, 0, flipAll)
                    b = find(tree.right, 0, flipAll)
                    ts.append(a + b + 1)
                # C2
                if True:
                    a = find(tree.left, 0, 1 - flipAll)
                    b = find(tree.right, 0, 1 - flipAll)
                    ts.append(a + b + 1)
                # C3
                if True:
                    a = find(tree.left, 1, flipAll)
                    b = find(tree.right, 1, flipAll)
                    ts.append(a + b + 1)
            else:
                # nothing.
                if True:
                    a = find(tree.left, 0, flipAll)
                    b = find(tree.right, 0, flipAll)
                    ts.append(a + b)
                # C1 + C2
                if True:
                    a = find(tree.left, 0, 1 - flipAll)
                    b = find(tree.right, 0, 1 - flipAll)
                    ts.append(a + b + 2)
                # C1 + C3
                if True:
                    a = find(tree.left, 1, flipAll)
                    b = find(tree.right, 1, flipAll)
                    ts.append(a + b + 2)
                # C2 + C3
                if True:
                    a = find(tree.left, 1, 1 - flipAll)
                    b = find(tree.right, 1, 1 - flipAll)
                    ts.append(a + b + 2)

            t = min(ts)
            return t

        ans = find(root, 0, 0)
        return ans


true, false, null = True, False, None
cases = [
]

import aatest_helper

cases.append([aatest_helper.list_to_tree(
    [1, 1, 1, 1, 1, 0, 1, null, null, null, 0, null, null, 1, 0, 1, 0, 1, 0, 0, null, null, null, 1, 1, 1, 1, 0, null,
     0, 0, null, null, 0, 0, null, null, null, null, 1, 1, null, null, 0, 0, null, null, null, null, 1, 1, 1, null, 1,
     1, null, null, null, null, 0, 1, 1, null, 0, null, null, null, null, 0, null, null, 1, 1, null, null, null, null,
     1, 1, 1, 1, 1, null, 0, 0, 0, null, null, null, 1, 0, null, null, null, null, 0, 1, 0, 0, null, null, 0, 1, 1, 0,
     0, null, null, null, null, null, null, null, 0, 0, null, null, 0, null, null, null, 0, 1, 0, 1, 1, 0, 0, 1, 1, 0,
     1, null, 0, 0, null, null, null, null, null, null, null, null, 0, 1, 0, 1, null, null, null, null, 1, null, null,
     null, 0, null, 1, 1, 0, 1, 1, 0, null, null, null, null, null, null, null, null, 1, 1, 1, 0, null, null, null,
     null, 0, 1, 1, null, null, null, 1, 0, 0, 0, null, null, null, null, 1, 0, 0, null, null, null, null, null, 1, 1,
     1, 1, 1, 0, 1, 1, 1, 1, 0, null, 0, 1, 1, 0, null, null, 1, null, 0, null, null, 0, null, null, 1, 1, null, null,
     null, null, null, null, 0, 1, 1, 1, null, 0, 1, null, null, null, null, null, 1, 0, null, null, 1, null, 0, null,
     null, null, 1, 1, 0, 1, null, 1, 1, 0, 1, null, null, null, 1, null, null, null, 1, 0, 1, null, null, 1, null,
     null, null, 0, null, null, 0, 0, 1, 0, null, 1, 1, 1, 1, 0, null, null, null, null, null, null, 0, 0, 0, 1, null,
     1, null, null, null, null, 0, 0, 0, 1, 0, 0, null, 0, null, null, null, 1, null, null, 1, 0, null, null, null,
     null, 1, null, null, 1, null, null, 1, 1, 1, 1, null, null, 0, 1, null, null, 0, null, 1, null, null, null, 0, 0,
     1, null, null, null, 1, 0, 0, null, null, null, null, null, 1, 0, 0, 1, null, null, null, null, 0, 1, 1, null, 0,
     1, null, 1, null, null, null, null, 0, 0, 1, 1, 0, 1, 0, null, null, 0, null, null, 0, 0, null, null, 0, null,
     null, null, 0, null, 0, null, null, 1, null, 0, null, null, 0, 1, null, null, 0, 0, null, 1, null, null, null, 1,
     null, null, 0, 0, 0, 1, 1, 0, 0, 0, null, 0, null, 0, 0, null, null, null, null, null, null, null, null, null, 1,
     null, 0, 0, null, null, 1]), 74])
aatest_helper.run_test_cases(Solution().closeLampInTree, cases)

if __name__ == '__main__':
    pass
